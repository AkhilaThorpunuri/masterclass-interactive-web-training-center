import os, re

BASE_DIR = r'c:\Code\masterclass-interactive-web-training-center'

# PySpark Module sequence
pyspark_sequence = [
    ('demo.html', 'Interactive Demo Lab', 'index.html', 'PySpark Overview', 'cluster-architecture.html', '1. Cluster Setup & Sizer'),
    ('cluster-architecture.html', '1. Cluster Setup & Sizer', 'index.html', 'PySpark Overview', 'data-distribution.html', '1b. Data Distribution & Splits'),
    ('data-distribution.html', '1b. Data Distribution & Splits', 'cluster-architecture.html', '1. Cluster Setup & Sizer', 'cloud-storage.html', '2. Cloud Storage Ingestion'),
    ('cloud-storage.html', '2. Cloud Storage Ingestion', 'data-distribution.html', '1b. Data Distribution & Splits', 'rdbms-jdbc.html', '3. Parallel RDBMS JDBC'),
    ('rdbms-jdbc.html', '3. Parallel RDBMS JDBC', 'cloud-storage.html', '2. Cloud Storage Ingestion', 'mpp-warehouses.html', '4. MPP Warehouses & Staging'),
    ('mpp-warehouses.html', '4. MPP Warehouses & Staging', 'rdbms-jdbc.html', '3. Parallel RDBMS JDBC', 'dag-execution.html', '5. DAG, Stages & Tasks'),
    ('dag-execution.html', '5. DAG, Stages & Tasks', 'mpp-warehouses.html', '4. MPP Warehouses & Staging', 'shuffle-partitioning.html', '6. Shuffle & Partitioning'),
    ('shuffle-partitioning.html', '6. Shuffle & Partitioning', 'dag-execution.html', '5. DAG, Stages & Tasks', 'shuffle-ops-lab.html', '6b. Shuffle Operations Lab'),
    ('shuffle-ops-lab.html', '6b. Shuffle Operations Lab', 'shuffle-partitioning.html', '6. Shuffle & Partitioning', 'shuffle-tuning-qna.html', '6c. Shuffle Tuning Q&A'),
    ('shuffle-tuning-qna.html', '6c. Shuffle Tuning Q&A', 'shuffle-ops-lab.html', '6b. Shuffle Operations Lab', 'streaming-cdc.html', '7. Streaming & CDC'),
    ('streaming-cdc.html', '7. Streaming & CDC', 'shuffle-tuning-qna.html', '6c. Shuffle Tuning Q&A', 'demo.html', 'Interactive Demo Lab')
]

def make_video_section(title):
    clean_title = title.replace('&amp;', '&').replace('&bull;', '•')
    return f'''      <!-- YouTube Lesson Video Placeholder: replace VIDEO_ID when the lesson is uploaded. -->
      <section id="lesson-video" class="py-video-section" aria-label="{clean_title} lesson video">
        <span class="py-eyebrow">VIDEO LESSON</span>
        <h2 class="py-h2" style="margin:8px 0 16px;">Watch the {clean_title} Lesson</h2>
        <div class="py-video-frame" data-youtube-video-placeholder>
          <div class="py-video-placeholder">
            <div class="py-video-play" aria-hidden="true">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
                <path d="M8 5v14l11-7z" />
              </svg>
            </div>
            <strong>YouTube video will be displayed here</strong>
            <span>After uploading the lesson, replace this placeholder with the YouTube embed URL.</span>
          </div>
        </div>
        <!-- Example: <iframe src="https://www.youtube-nocookie.com/embed/VIDEO_ID" title="{clean_title} lesson" allowfullscreen></iframe> -->
      </section>'''

def make_modnav(prev_href, prev_title, next_href, next_title):
    return f'''      <!-- Module Navigation: Back on bottom left, Next module on bottom right -->
      <nav class="py-modnav" id="py-modnav" aria-label="Module navigation">
        <a href="{prev_href}">
          <span>&larr; Back</span>
          <strong>{prev_title}</strong>
        </a>
        <a class="next" href="{next_href}" style="--mod-accent:#38bdf8;">
          <span>Next module &rarr;</span>
          <strong>{next_title}</strong>
        </a>
      </nav>'''

# 1. Process PySpark track files
for fname, title, p_href, p_title, n_href, n_title in pyspark_sequence:
    fpath = os.path.join(BASE_DIR, 'pyspark', fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    changed = False

    # Video placeholder insertion
    if 'id="lesson-video"' not in c and 'py-video-section' not in c:
        v_sec = make_video_section(title)
        # Look for end of hero or first section
        hero_patterns = [
            r'(<section[^>]*class="[^"]*hero[^"]*"[^>]*>.*?</section>)',
            r'(<div[^>]*class="[^"]*hero[^"]*"[^>]*>.*?</div>)',
            r'(<section[^>]*class="[^"]*dd-hero[^"]*"[^>]*>.*?</section>)',
            r'(<div[^>]*class="[^"]*pyspark-page-hero[^"]*"[^>]*>.*?</div>)',
            r'(<section[^>]*id="sec-(?:race|lab-overview|overview)"[^>]*>)'
        ]
        inserted = False
        for hp in hero_patterns:
            m = re.search(hp, c, re.DOTALL | re.IGNORECASE)
            if m:
                # If it matched an opening tag of sec-race/sec-overview, insert before it
                if m.group(0).startswith('<section id="sec-'):
                    idx = m.start()
                    c = c[:idx] + v_sec + '\n\n      ' + c[idx:]
                else:
                    idx = m.end()
                    c = c[:idx] + '\n\n' + v_sec + c[idx:]
                inserted = True
                changed = True
                print(f"Inserted video into pyspark/{fname}")
                break
        if not inserted:
            # Fallback: after <main ...>
            m_main = re.search(r'<main[^>]*>', c, re.IGNORECASE)
            if m_main:
                idx = m_main.end()
                c = c[:idx] + '\n\n' + v_sec + '\n' + c[idx:]
                changed = True
                print(f"Fallback inserted video into pyspark/{fname}")

    # Modnav insertion
    if 'id="py-modnav"' not in c and 'class="py-modnav"' not in c:
        modnav_str = make_modnav(p_href, p_title, n_href, n_title)
        m_main_end = c.rfind('</main>')
        if m_main_end != -1:
            c = c[:m_main_end] + modnav_str + '\n\n    ' + c[m_main_end:]
            changed = True
            print(f"Inserted modnav into pyspark/{fname}")

    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)

print("Completed PySpark sequence updates.")

