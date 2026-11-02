"""Apply unified ROG background, header, and appearance across all courses."""
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = {"sales-pitch", "pdfs", "node_modules", "tools"}

UNIFIED_CSS_INJECTION = """
/* =============================================================================
   UNIFIED ROG DEEP TEAL THEME & APPEARANCE SYSTEM
   ============================================================================= */
:root,
:root[data-theme="light"],
[data-theme="light"] {
  --why-bg: #032532;
  --why-bg-2: #073443;
  --why-card: rgba(3, 28, 42, .90);
  --why-card-hi: rgba(5, 42, 59, .94);
  --why-line: rgba(76, 218, 239, .30);
  --why-text: #effaff;
  --why-muted: #c8e2eb;
  --why-dim: #9bbdc9;
  --why-cyan: #67e2f2;

  --ref-box-bg: #05304b;
  --ref-box-bg-deep: #04283f;
  --ref-box-border: rgba(28, 137, 166, .78);
  --ref-box-heading: #f2f8fc;
  --ref-box-text: #c9dce8;
  --ref-box-muted: #a9c4d3;
  --ref-box-accent: #35d0a0;

  --bg-dark: #032532 !important;
  --bg-surface: #05304b !important;
  --bg-card: rgba(5, 48, 75, 0.90) !important;
  --bg-card-hover: rgba(8, 62, 95, 0.94) !important;
  --bg-elevated: #063958 !important;
  --bg-body: #032532 !important;
  --border-color: rgba(28, 137, 166, 0.65) !important;
  --border-subtle: rgba(76, 218, 239, 0.25) !important;
  --text-main: #effaff !important;
  --text-muted: #c8e2eb !important;
  --text-dim: #9bbdc9 !important;
  --text-color: #effaff !important;

  --md-surface: #032532 !important;
  --md-surface-lowest: #05304b !important;
  --md-surface-low: #04283f !important;
  --md-surface-c: #06344f !important;
  --md-surface-high: #08415e !important;
  --md-surface-highest: #0a4f73 !important;
  --md-on-surface: #effaff !important;
  --md-on-surface-var: #c8e2eb !important;
  --md-outline: rgba(76, 218, 239, 0.4) !important;
  --md-outline-var: rgba(28, 137, 166, 0.78) !important;
}

html,
body,
[data-theme="light"] body,
body.pa-theme,
body.theme-dark,
body.hx-body {
  min-height: 100%;
  background-color: #032532 !important;
  color: #effaff !important;
}

body,
[data-theme="light"] body,
body.pa-theme,
body.theme-dark,
body.hx-body {
  position: relative !important;
  isolation: isolate !important;
  background-image:
    radial-gradient(ellipse at 50% 30%, rgba(0, 119, 145, .22), transparent 58%),
    radial-gradient(ellipse at 8% 82%, rgba(10, 92, 111, .17), transparent 45%),
    linear-gradient(135deg, #042b38 0%, #032431 48%, #052c3a 100%) !important;
  background-attachment: fixed !important;
}

#rog-connection-canvas {
  position: fixed !important;
  inset: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  display: block !important;
  z-index: -1 !important;
  pointer-events: none !important;
  opacity: .48 !important;
  mix-blend-mode: screen !important;
}

/* -----------------------------------------------------------------------------
   MASTER TOP NAVIGATION BAR (DARK ROG TEAL THEME)
   ----------------------------------------------------------------------------- */
.master-top-nav,
body.pa-theme .master-top-nav,
[data-theme="light"] .master-top-nav {
  position: sticky !important;
  top: 0 !important;
  z-index: 1000 !important;
  width: 100% !important;
  overflow: visible !important;
  isolation: isolate !important;
  background: linear-gradient(105deg,
      rgba(10, 25, 48, .985) 0%,
      rgba(17, 43, 75, .98) 48%,
      rgba(12, 54, 68, .98) 100%) !important;
  border-bottom: 1px solid rgba(125, 180, 232, .32) !important;
  box-shadow: 0 8px 28px rgba(5, 18, 36, .30) !important;
  backdrop-filter: blur(18px) !important;
  -webkit-backdrop-filter: blur(18px) !important;
}

.master-top-nav::after {
  content: "" !important;
  position: absolute !important;
  left: 0 !important;
  right: 0 !important;
  bottom: -1px !important;
  height: 2px !important;
  pointer-events: none !important;
  background: linear-gradient(90deg, transparent 0%,
      rgba(96, 165, 250, .85) 28%,
      rgba(45, 212, 191, .80) 70%,
      transparent 100%) !important;
}

.master-top-nav,
.master-top-nav * {
  box-sizing: border-box !important;
}

.master-top-nav-inner {
  position: relative !important;
  z-index: 2 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
  gap: clamp(8px, 1vw, 16px) !important;
  padding: 10px clamp(12px, 2.2vw, 32px) !important;
  overflow: visible !important;
  flex-wrap: nowrap !important;
}

.master-brand-wrap {
  display: flex !important;
  align-items: center !important;
  flex: 1 1 0 !important;
  min-width: 0 !important;
  max-width: none !important;
  gap: clamp(8px, 1.2vw, 18px) !important;
  text-decoration: none !important;
}

.master-brand-logo {
  display: block !important;
  flex: 0 1 auto !important;
  width: clamp(165px, 21vw, 285px) !important;
  max-width: 100% !important;
  height: auto !important;
  max-height: 42px !important;
  object-fit: contain !important;
  filter: drop-shadow(0 2px 5px rgba(0, 0, 0, 0.3)) !important;
}

.master-brand-badge,
body.pa-theme .master-brand-badge,
[data-theme="light"] .master-brand-badge {
  flex: 0 0 auto !important;
  max-width: 190px !important;
  white-space: nowrap !important;
  color: #D6E9FF !important;
  background: rgba(96, 165, 250, .13) !important;
  border: 1px solid rgba(147, 197, 253, .34) !important;
  border-radius: 6px !important;
  padding: 5px 12px !important;
  font-size: 0.88rem !important;
  font-weight: 800 !important;
  letter-spacing: 0.05em !important;
  text-transform: uppercase !important;
  box-shadow: none !important;
}

.master-menu-links {
  position: relative !important;
  z-index: 3 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex: 0 0 auto !important;
  min-width: max-content !important;
  gap: 8px !important;
  overflow: visible !important;
  margin: 0 !important;
  padding: 0 !important;
  list-style: none !important;
}

.master-nav-btn,
.master-dropdown-toggle,
[data-theme="light"] .master-nav-btn,
[data-theme="light"] .master-dropdown-toggle {
  color: #D8E6F6 !important;
  background: rgba(255, 255, 255, .055) !important;
  border: 1px solid rgba(191, 219, 254, .17) !important;
  border-radius: 8px !important;
  padding: 8px 12px !important;
  white-space: nowrap !important;
  font-size: 0.86rem !important;
  font-weight: 600 !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 7px !important;
  cursor: pointer !important;
  text-decoration: none !important;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.master-nav-btn svg,
.master-dropdown-toggle svg {
  color: #8FC5FF !important;
}

.master-nav-btn:hover,
.master-dropdown-toggle:hover,
.master-dropdown.open .master-dropdown-toggle,
[data-theme="light"] .master-nav-btn:hover,
[data-theme="light"] .master-dropdown-toggle:hover,
[data-theme="light"] .master-dropdown.open .master-dropdown-toggle {
  color: #FFFFFF !important;
  background: rgba(96, 165, 250, .18) !important;
  border-color: rgba(125, 190, 255, .52) !important;
}

.master-dropdown {
  position: relative !important;
  z-index: 1002 !important;
  overflow: visible !important;
  display: inline-block !important;
}

.master-dropdown-menu {
  position: absolute !important;
  top: calc(100% + 8px) !important;
  z-index: 2000 !important;
  max-width: calc(100vw - 24px) !important;
  background: rgba(239, 249, 252, .99) !important;
  color: #234967 !important;
  border: 1px solid rgba(69, 158, 184, .35) !important;
  box-shadow: 0 16px 38px rgba(0, 20, 34, .24) !important;
  backdrop-filter: blur(18px) !important;
  -webkit-backdrop-filter: blur(18px) !important;
  border-radius: 14px !important;
}

.master-dropdown-menu a,
.master-dropdown-menu button {
  color: #234967 !important;
}

.master-dropdown-menu a:hover,
.master-dropdown-menu button:hover {
  color: #073b57 !important;
  background: rgba(91, 207, 224, .20) !important;
}

.master-dropdown-menu.mega-menu {
  left: 50% !important;
  transform: translateX(-50%) !important;
  width: 1280px !important;
  max-width: calc(100vw - 32px) !important;
  background: rgba(239, 249, 252, .99) !important;
  border: 1.5px solid rgba(69, 158, 184, .45) !important;
  padding: 0 !important;
}

.mega-menu-header {
  background: rgba(215, 238, 245, 0.7) !important;
  border-bottom: 1px solid rgba(69, 158, 184, .25) !important;
}

.mega-menu-eyebrow {
  color: #087a9a !important;
}

.mega-menu-title {
  color: #10354c !important;
}

.mega-menu-stats-pill {
  color: #1b4b66 !important;
  background: rgba(255, 255, 255, 0.8) !important;
  border: 1px solid rgba(69, 158, 184, .3) !important;
}

.mega-category-col {
  background: rgba(255, 255, 255, 0.55) !important;
  border: 1px solid rgba(139, 202, 220, 0.45) !important;
}

.mega-category-col:hover {
  background: rgba(255, 255, 255, 0.9) !important;
  border-color: rgba(69, 158, 184, .6) !important;
}

.mega-category-item {
  color: #234967 !important;
}

.mega-category-item:hover {
  background: rgba(91, 207, 224, .20) !important;
  color: #073b57 !important;
}

.mega-item-icon {
  background: rgba(255, 255, 255, 0.8) !important;
  color: #087a9a !important;
}

.mega-menu-footer {
  background: rgba(215, 238, 245, 0.85) !important;
  border-top: 1px solid rgba(69, 158, 184, .25) !important;
  color: #234967 !important;
}

.mega-footer-left strong,
.mega-footer-right strong {
  color: #10354c !important;
}

.master-nav-actions {
  display: flex !important;
  align-items: center !important;
  justify-content: flex-end !important;
  flex: 0 1 auto !important;
  min-width: 0 !important;
  margin-left: 0 !important;
  gap: clamp(5px, .65vw, 10px) !important;
  white-space: nowrap !important;
}

.master-instructor-beam {
  flex: 0 1 auto !important;
  min-width: 0 !important;
  max-width: clamp(165px, 18vw, 245px) !important;
  padding: 8px clamp(7px, .8vw, 12px) !important;
  gap: 6px !important;
  white-space: nowrap !important;
  background: rgba(255, 255, 255, .075) !important;
  border: 1px solid rgba(191, 219, 254, .22) !important;
}

.master-instructor-beam .inst-label {
  color: #c8e2eb !important;
}

.master-instructor-beam .inst-name {
  color: #ffffff !important;
}

.master-nav-social-btn {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex: 0 0 auto !important;
  gap: 6px !important;
  padding: 8px 10px !important;
  white-space: nowrap !important;
  color: #D8E6F6 !important;
  background: rgba(255, 255, 255, .075) !important;
  border: 1px solid rgba(191, 219, 254, .22) !important;
  border-radius: 10px !important;
  text-decoration: none !important;
}

.master-nav-social-btn:hover {
  color: #FFFFFF !important;
  background: rgba(96, 165, 250, .18) !important;
  border-color: rgba(125, 190, 255, .52) !important;
}

@media (max-width: 1380px) and (min-width: 1061px) {
  .master-top-nav-inner {
    gap: 7px !important;
    padding-inline: 12px !important;
  }
  .master-brand-logo {
    width: clamp(150px, 17vw, 225px) !important;
  }
  .master-brand-badge {
    font-size: 10px !important;
    padding: 6px 8px !important;
  }
  .master-nav-btn,
  .master-dropdown-toggle {
    padding: 7px 8px !important;
    font-size: 11px !important;
  }
  .master-instructor-beam {
    max-width: 185px !important;
    font-size: 11px !important;
  }
  .master-nav-social-btn {
    padding: 7px 8px !important;
    font-size: 11px !important;
  }
}

@media (max-width: 1060px) {
  .master-top-nav-inner {
    flex-wrap: wrap !important;
    justify-content: space-between !important;
    row-gap: 8px !important;
  }
  .master-brand-wrap {
    flex: 1 1 48% !important;
    max-width: none !important;
  }
  .master-menu-links {
    order: 3 !important;
    flex: 1 0 100% !important;
    justify-content: flex-start !important;
  }
  .master-nav-actions {
    flex: 0 1 auto !important;
    margin-left: auto !important;
  }
}

@media (max-width: 640px) {
  .master-top-nav-inner {
    padding: 8px 10px !important;
  }
  .master-brand-logo {
    width: clamp(132px, 38vw, 190px) !important;
    max-height: 34px !important;
  }
  .master-brand-badge {
    display: none !important;
  }
  .master-nav-actions {
    flex: 1 0 100% !important;
    width: 100% !important;
    justify-content: flex-start !important;
    order: 2 !important;
    gap: 7px !important;
  }
  .master-instructor-beam {
    max-width: min(52vw, 220px) !important;
  }
  .master-nav-social-btn {
    padding: 7px 10px !important;
  }
  .master-menu-links {
    order: 3 !important;
    overflow-x: auto !important;
    scrollbar-width: thin;
    padding-bottom: 2px !important;
  }
}

@media (max-width: 390px) {
  .master-instructor-beam {
    max-width: 145px !important;
  }
  .master-instructor-beam .inst-label {
    display: none !important;
  }
  .master-nav-social-btn {
    padding: 7px 8px !important;
  }
}

/* -----------------------------------------------------------------------------
   UNIFIED NAVY-TEAL CONTENT SURFACES, CARDS & PANELS
   ----------------------------------------------------------------------------- */
.subject-hero-card,
.subject-hero,
.demo-hero,
.hub-header,
.course-hero,
.sf-hero,
.py-hero,
.pa-hero,
.pillars-matrix-grid>div,
.job-market-box,
.page-main-wrap>section,
.page-main-wrap .card,
.page-main-wrap .panel,
.page-main-wrap .feature-card,
.page-main-wrap .info-card,
.page-main-wrap .content-card,
.page-main-wrap .step-card,
.page-main-wrap .module-card,
.page-main-wrap .demo-card,
.page-main-wrap .why-card,
.page-main-wrap .topic-card,
.page-main-wrap .lab-card,
.module-card,
.topic-card,
.demo-card,
.why-card,
.step-card,
.concept-card,
.sf-card,
.sf-module,
.sf-callout,
.pa-card,
.pa-action-card,
.pa-stage-card,
.ag-card,
.agent-card,
.sdk-card,
.harness-card,
.stack-card,
.project-card,
.tier-card,
.exec-box,
.stat-card,
.cluster-calc-card,
.shuffle-card,
.qna-card,
.sidebar-topics-nav,
.sidebar-inpage-nav,
.sidebar-panel,
.sidebar-box,
.pa-side,
.pa-toc,
.card,
.panel,
.content-box,
.info-box,
.callout-box,
.master-layout-3col .sidebar-topics-nav,
.master-layout-3col .sidebar-inpage-nav,
[data-theme="light"] .sidebar-topics-nav,
[data-theme="light"] .sidebar-inpage-nav,
[data-theme="light"] .step-card,
[data-theme="light"] .module-card {
  color: var(--ref-box-text) !important;
  background:
    radial-gradient(ellipse at 88% 4%, rgba(29, 130, 166, .16), transparent 48%),
    linear-gradient(135deg, #06344f 0%, #052f4a 55%, #04283f 100%) !important;
  border: 1px solid var(--ref-box-border) !important;
  box-shadow:
    0 14px 34px rgba(0, 12, 24, .25),
    inset 0 1px 0 rgba(174, 229, 244, .08) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
}

h1, h2, h3, h4,
.subject-hero-card h1, .subject-hero-card h2, .subject-hero-card h3,
.subject-hero h1, .subject-hero h2, .subject-hero h3,
.demo-hero h1, .demo-hero h2, .demo-hero h3,
.sf-title, .sf-section-head h2, .sf-main h3, .sf-main h4,
.pillars-matrix-grid h3,
.job-market-box h3, .job-market-box h4,
.page-main-wrap h1, .page-main-wrap h2, .page-main-wrap h3, .page-main-wrap h4,
.page-main-wrap .card h1, .page-main-wrap .card h2, .page-main-wrap .card h3,
.page-main-wrap .panel h1, .page-main-wrap .panel h2, .page-main-wrap .panel h3,
.module-card h3, .topic-card h3, .demo-card h3, .why-card h3, .sf-card h3, .pa-card h3,
.sf-module h4, .sf-card-title,
[data-theme="light"] .card-title,
[data-theme="light"] .step-title {
  color: var(--ref-box-heading) !important;
}

p, li, label,
.subject-hero-card p,
.pillars-matrix-grid p,
.job-market-box p, .job-market-box li,
.page-main-wrap p, .page-main-wrap li,
.page-main-wrap .card p, .page-main-wrap .panel p,
.module-card p, .topic-card p, .demo-card p, .why-card p, .sf-card p, .pa-card p,
.sf-lead, .sf-card p, .sf-card li, .sf-module ul,
[data-theme="light"] .card-description,
[data-theme="light"] .step-desc {
  color: var(--ref-box-text) !important;
}

.sf-chip, .sf-eyebrow, .subject-badge-pill, .demo-badge-pill, .module-num-tag, .sf-module-num {
  color: #d8f1f8 !important;
  background: rgba(8, 67, 91, .82) !important;
  border: 1px solid rgba(74, 181, 205, .38) !important;
  border-radius: 999px !important;
  padding: 3px 10px !important;
}

.btn-primary, .cta-btn, .module-cta-btn, .run-btn, #btn-run {
  background: linear-gradient(135deg, #087f9f, #126b8c) !important;
  color: #ffffff !important;
  border: 1px solid rgba(103, 226, 242, 0.45) !important;
  box-shadow: 0 8px 20px rgba(0, 125, 160, .28) !important;
}

.btn-secondary, .step-btn, #btn-step {
  color: #dff7ff !important;
  background: rgba(19, 104, 132, .35) !important;
  border: 1px solid rgba(103, 226, 242, .34) !important;
}

a {
  color: #82e4f2;
}

a:hover {
  color: #c0f5ff;
}

table {
  color: var(--ref-box-text) !important;
  background: #05304b !important;
  border-color: var(--ref-box-border) !important;
}

th {
  color: var(--ref-box-heading) !important;
  background: #08415e !important;
}

td {
  color: var(--ref-box-text) !important;
  background: rgba(5, 48, 75, .94) !important;
}

pre, code {
  color: #a5f3fc !important;
  background: #031f33 !important;
  border-color: rgba(28, 137, 166, 0.45) !important;
}

.sidebar-topic-link {
  color: #c9dce8 !important;
}

.sidebar-topic-link:hover,
[data-theme="light"] .sidebar-topic-link:hover {
  color: #ffffff !important;
  background: rgba(255, 255, 255, 0.08) !important;
}

.sidebar-topic-link.active,
[data-theme="light"] .sidebar-topic-link.active {
  color: #ffffff !important;
  background: rgba(30, 160, 190, 0.28) !important;
  border-color: rgba(76, 218, 239, 0.6) !important;
}

.sidebar-topic-badge {
  background: rgba(255, 255, 255, 0.08) !important;
  color: #c8e2eb !important;
}

.sidebar-topic-link.active .sidebar-topic-badge {
  background: #087a9a !important;
  color: #ffffff !important;
}

/* -----------------------------------------------------------------------------
   VIDEO LESSON SECTION & PLACEHOLDER THEME
   ----------------------------------------------------------------------------- */
.py-video-section,
.video-section,
#lesson-video,
[data-video-section] {
  width: 100% !important;
  background:
    radial-gradient(ellipse at 88% 4%, rgba(29, 130, 166, .16), transparent 48%),
    linear-gradient(135deg, #06344f 0%, #052f4a 55%, #04283f 100%) !important;
  border: 1px solid var(--ref-box-border) !important;
  border-radius: 14px !important;
  box-shadow: 0 14px 34px rgba(0, 12, 24, .25), inset 0 1px 0 rgba(174, 229, 244, .08) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
}

.py-video-placeholder,
.video-placeholder {
  background: rgba(4, 30, 48, 0.78) !important;
  border: 1px dashed rgba(76, 218, 239, 0.42) !important;
  border-radius: 12px !important;
  color: #c9dce8 !important;
}

.py-video-play,
.video-play {
  background: linear-gradient(135deg, #087f9f, #126b8c) !important;
  box-shadow: 0 0 20px rgba(103, 226, 242, 0.35) !important;
  color: #ffffff !important;
}

/* -----------------------------------------------------------------------------
   BOTTOM MODULE NAVIGATION STRIP
   ----------------------------------------------------------------------------- */
.py-modnav,
.course-modnav,
#py-modnav {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 16px !important;
  width: 100% !important;
}

.py-modnav> :first-child,
.course-modnav> :first-child {
  margin-right: auto !important;
}

.py-modnav> :last-child,
.course-modnav> :last-child {
  margin-left: auto !important;
}

.py-modnav-link {
  display: inline-flex !important;
  align-items: center !important;
  gap: 12px !important;
  padding: 12px 18px !important;
  background: #0d1b31 !important;
  border: 1px solid rgba(103, 226, 242, 0.32) !important;
  border-radius: 10px !important;
  color: #e6f6ff !important;
  text-decoration: none !important;
  box-shadow: 0 4px 16px rgba(0, 18, 30, 0.35) !important;
}

.py-modnav-link:hover {
  background: #112847 !important;
  border-color: #67e2f2 !important;
  box-shadow: 0 0 16px rgba(103, 226, 242, 0.4) !important;
}
"""


def update_master_layout_css():
    css_path = ROOT / "assets" / "css" / "master-global-layout.css"
    content = css_path.read_text(encoding="utf-8")
    
    # We replace or append UNIFIED_CSS_INJECTION
    marker = "/* =============================================================================\n   UNIFIED ROG DEEP TEAL THEME & APPEARANCE SYSTEM"
    if marker in content:
        content = content[:content.index(marker)]
    
    content = content.rstrip() + "\n\n" + UNIFIED_CSS_INJECTION.strip() + "\n"
    css_path.write_text(content, encoding="utf-8", newline="\n")
    print(f"Updated {css_path}")


def add_canvas_to_html_pages():
    canvas_markup = '\n  <canvas id="rog-connection-canvas" aria-hidden="true"></canvas>'
    canvas_re = re.compile(r'id=["\']rog-connection-canvas["\']')
    body_re = re.compile(r'(<body\b[^>]*>)', re.IGNORECASE)

    updated_count = 0
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT)
        if rel.parts[0] in SKIP_DIRS or rel == pathlib.Path("index.html"):
            continue

        html = path.read_text(encoding="utf-8")
        if canvas_re.search(html):
            continue

        m = body_re.search(html)
        if not m:
            continue

        insert_pos = m.end()
        new_html = html[:insert_pos] + canvas_markup + html[insert_pos:]
        path.write_text(new_html, encoding="utf-8", newline="\n")
        updated_count += 1

    print(f"Added rog-connection-canvas to {updated_count} HTML pages")


if __name__ == "__main__":
    update_master_layout_css()
    add_canvas_to_html_pages()
