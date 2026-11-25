'use strict';
// Each narrated scene is grounded in content discovered on the real page, not
// an LLM guess about what a button might do. Page-specific adapters can extend
// this neutral, repeatable plan.
const strip = value => String(value || '').replace(/\s+/g, ' ').trim();
const brief = (value, limit=210) => {
  const text=strip(value);
  if(text.length<=limit)return text;
  const part=text.slice(0,limit);
  return part.slice(0,Math.max(part.lastIndexOf('. ')+1,part.lastIndexOf('; ')+1,Math.floor(limit*.7))) || part;
};
function overview(slides=[],name='this lesson'){
  const names=slides.map(s=>s.title).filter(Boolean);
  if(!names.length)return `This is ${name}. Explore the explanation, change a value, and compare the resulting output.`;
  const sample=names.slice(0,3).join(', ');
  return `This module covers ${names.length} topics, including ${sample}${names.length>3?', and more':''}.`;
}
function teachSlide(s,opts={}){
  const name=strip(s.title)||'this topic';
  if(opts.concise){
    const budget=opts.maxChars||145;
    const key=brief(s.idea,Math.min(115,budget));
    const detail=brief(s.explain||s.analogy||'',Math.max(55,budget-key.length));
    const parts=[`${name}.`,key];
    if(detail && !key.toLowerCase().includes(detail.toLowerCase()) && (key.length+detail.length)<=budget+25){
      parts.push(detail);
    }
    return parts.filter(Boolean).join(' ').replace(/\s+/g,' ').trim();
  }
  const key=brief(s.idea,210);
  const analogy=brief(s.analogy,170);
  const explain=brief(s.explain,210);
  const out=brief(s.output,120);
  const example=brief(s.code,100);
  let lines=[`${name}.`,key];
  if(analogy && analogy.toLowerCase()!==key.toLowerCase())lines.push(analogy);
  if(explain && !key.includes(explain))lines.push(explain);
  if(example && opts.code)lines.push(`The example uses ${example}.`);
  if(out && opts.output)lines.push(`The expected output is ${out}.`);
  const tip=brief(s.tip,150);
  if(tip && opts.tip)lines.push(tip);
  return lines.filter(Boolean).join(' ').replace(/\s+/g,' ').trim();
}
function sequence(page,manifest){
 const scenes=[];
 const push=(title,target,action,narration,stage=null,opts={})=>scenes.push({title,target,action,narration,stage:stage||manifest.anchor,holdMs:900,...opts});
 const heading=manifest.title||'this interactive dashboard';
 if(manifest.adapter==='pycourse'){
  const slides=Array.isArray(manifest.slides)?manifest.slides:[];
  const isSql=/(?:^|\/)sql\//i.test(page);
  // Keep every module video under 5 minutes (<300s) by scaling per-slide script length to slide count.
  const slideBudget=slides.length>=14?125:slides.length>=10?145:165;
  const slideFocusSteps=isSql?['#py-stage .py-idea','#py-stage .py-anim','#py-stage .py-code-col']:['#py-stage .py-idea','#py-stage .py-anim','#py-stage .py-code-col'];
  push('Welcome to the dashboard','#dashboard','show',`Welcome to ${heading}. ${overview(slides,heading)}`,'#dashboard');
  push('What this dashboard contains','#py-learn','show',`Select any topic here to jump straight to its interactive example.`,'#dashboard');
  push('Your progress','#py-stat-progress','show','The completion meter tracks the slides you have opened in this browser.','#dashboard');
  push('Start learning','#py-continue','click',`Let us open the lesson and explore the interactive slides.`,'#dashboard');
  push('Return to slide one','#py-first','click','Starting at slide one.','#player',{skipAudio:true,holdMs:550});
  if(slides[0])push('Understand the first topic','#py-stage','show',teachSlide(slides[0],{concise:true,maxChars:slideBudget+20}),'#player',{conceptIndex:0,focusSteps:['#py-stage .py-idea','#py-stage .py-anim']});
  push('The code editor','#py-editor','show',isSql?'On the right is the editable SQL query, running on real PostgreSQL in your browser.':'On the right is the editable Python code editor. You can modify any example and run it.','#player');
  push('Run the code','#py-run','click',isSql?'Click Run to execute the SQL query.':'Click Run to execute the Python code.','#player',{verify:'#py-term'});
  push('Read the output','#py-term','show',isSql?'This panel shows what PostgreSQL returns for each statement.':`This panel shows the program output.${slides[0]?.output?` Here it prints ${brief(slides[0].output,70)}.`:''}`,'#player');
  if(isSql){
   push('Inspect the database','#sql-db','show','Below it, the database panel shows your live schema, tables, and any new, changed, or removed rows.','#player');
  }
  if(/\/print(?:-v\d+)?\.html$/.test('/'+page)){ /* AUTO_TUTOR_V1 */
   push('Edit an example','#py-editor','edit','Let us change the printed message inside the quotation marks.','#player',{value:'print("I can use Python!")'});
   push('Run the edited example','#py-run','click','Run the updated code to see I can use Python in the output.','#player',{verify:'#py-term',expectContains:'I can use Python!'});
   push('Reset the example','#py-reset-code','click','Reset restores the original slide example.','#player');
  }
  push('Open the next topic','#py-next','click',slides[1]?`Next: ${slides[1].title}.`:'Moving to the next slide.','#player',{skipAudio:true,holdMs:600});
  if(slides[1])push('Learn topic 2','#py-stage','show',teachSlide(slides[1],{concise:true,maxChars:slideBudget}),'#player',{conceptIndex:1,focusSteps:slideFocusSteps});
  // Every discovered lesson is explained concisely while highlighting its concept and code panels.
  for(let i=2;i<slides.length;i++){
    const s=slides[i];
    push(`Open slide ${i+1}: ${s.title}`,'#py-next','click',`Slide ${i+1}: ${s.title}`,'#player',{conceptIndex:i,skipAudio:true,holdMs:550});
    push(`Teach slide ${i+1}: ${s.title}`,'#py-stage','show',teachSlide(s,{concise:true,maxChars:slideBudget}),'#player',{conceptIndex:i,focusSteps:slideFocusSteps});
  }
  if(slides.length)push('Finish the walkthrough','#py-outline','show',`That completes all ${slides.length} topics in ${heading}. Edit the examples and use Run and Reset to practice.`,'#player');
 }else{
  const anchor=manifest.anchor==='main'?'main':manifest.anchor;
  const facts=manifest.pageOverview || {};
  const headings=(facts.headings||[]).filter(Boolean).slice(0,5);
  const intro=headings.length?`The dashboard includes ${headings.join(', ')}.`:'We will identify the major components and see how the visualization changes.';
  push('Introducing the dashboard',anchor,'show',`Welcome to ${heading}. ${brief(intro,360)} This tour explains both the purpose of the content and how its controls work.`,anchor);
  const controls=(manifest.liveControls||[]).filter(x=>!x.disabled&&x.tag==='button');
  const oldControls=(manifest.candidateControls||[]).map(selector=>({selector,label:selector}));
  const usable=controls.length?controls:oldControls;
  const find=(pattern)=>usable.find(c=>pattern.test(c.label+' '+c.selector))?.selector||null;
  const run=find(/(?:run|play|execute|kick|start)/i),step=find(/(?:step|next)/i),reset=find(/reset/i);
  if(run){
   const desc=/pyspark|dag/i.test(page)?'This is a Spark execution graph. A job is divided into stages, and each stage runs tasks. Watch what changes when an operation reaches a shuffle boundary.':/\/apis\//i.test(page)?'This architecture demonstrates how an API request moves through processing stages. Observe the request, the response and the log output.':/full-stack/i.test(page)?'This demonstrates how application components process a request. Watch the flow from the client to the services and back.':'Run the demonstration to see the flow change. Pay attention to the intermediate steps, not just the final result.';
   push('Understand and run the simulation',run,'click',desc,anchor);
  }
  if(step&&step!==run)push('Understand one step',step,'click',/pyspark|dag/i.test(page)?'Stepping forward shows how the next DAG operation activates. Each stage depends on the results of earlier tasks.':'Step through one operation at a time and observe which component becomes active.',anchor);
  if(reset)push('Restore the starting state',reset,'click','Reset returns the simulator to its starting state so you can experiment with a different sequence.',anchor);
  if(!run&&!step){const b=usable.find(x=>!/(delete|remove|clear|logout|submit|pay|transfer|send|publish|install|purchase)/i.test(x.label));if(b)push('Explore a control',b.selector,'click',`This is the ${b.label.replace(/[<>]/g,'')} control. Notice which part of the dashboard responds when it is selected.`,anchor);}
  if(headings.length)push('What you learned',anchor,'show',`Review the main concepts: ${headings.join(', ')}. These pieces work together to explain the dashboard's subject.`,anchor);
  push('Try it yourself',anchor,'show','Now explore at your own pace. Change one input at a time, observe its effect, and use Reset where available.',anchor);
 }

 return scenes;
}
module.exports={sequence,teachSlide,overview,brief};
