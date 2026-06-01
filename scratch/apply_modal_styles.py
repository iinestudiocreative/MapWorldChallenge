def main():
    # ─── PART 1: Update index.html ──────────────────────────────
    with open("index.html", "r", encoding="utf-8") as f:
        content_html = f.read()

    # Re-design #tutorial-overlay in index.html to match custom-modal
    old_tutorial_html = """<!-- ═══════════════════════════════════════════ TUTORIAL POPUP MODAL -->
<div id="tutorial-overlay" class="hidden">
  <div id="tutorial-modal">
    <h3 id="tuto-title">Bienvenue sur Ride the world ! 🌍</h3>
    <div id="tuto-steps">
      <div class="tuto-step">
        <div class="tuto-icon"><i class="fa-solid fa-maximize"></i></div>
        <div class="tuto-text">
          <strong id="tuto-step1-title">Zoomer & Déplacer</strong>
          <span id="tuto-step1-desc">Pincez avec 2 doigts ou utilisez la molette de la souris pour naviguer sur la carte.</span>
        </div>
      </div>
      <div class="tuto-step">
        <div class="tuto-icon"><i class="fa-solid fa-location-dot"></i></div>
        <div class="tuto-text">
          <strong id="tuto-step2-title">Sélectionner un Statut</strong>
          <span id="tuto-step2-desc">Cliquez sur une région ou un département pour enregistrer votre niveau d'exploration.</span>
        </div>
      </div>
      <div class="tuto-step">
        <div class="tuto-icon"><i class="fa-solid fa-share-nodes"></i></div>
        <div class="tuto-text">
          <strong id="tuto-step3-title">Exporter & Partager</strong>
          <span id="tuto-step3-desc">Cliquez sur le bouton d'export pour télécharger une superbe carte prête pour vos réseaux sociaux !</span>
        </div>
      </div>
    </div>
    <button id="btn-tuto-close">C'est parti !</button>
  </div>
</div>"""

    new_tutorial_html = """<!-- ═══════════════════════════════════════════ TUTORIAL POPUP MODAL -->
<div id="tutorial-overlay" class="hidden">
  <div id="tutorial-modal" class="custom-modal">
    <div class="modal-header">
      <h3 id="tuto-title">Bienvenue</h3>
      <button id="btn-tuto-header-close" class="modal-close">✕</button>
    </div>
    <p id="modal-sub" style="margin-top: -6px; margin-bottom: 20px;">Comment utiliser l'application</p>
    
    <div class="modal-opts" id="tuto-steps">
      <!-- Step 1 -->
      <div class="opt-btn" style="cursor: default; pointer-events: none;">
        <span class="opt-dot" style="display: flex; align-items: center; justify-content: center; background: #e5e7eb; border: none; font-size: 0.8rem; width: 24px; height: 24px; color: #111111;"><i class="fa-solid fa-maximize"></i></span>
        <div>
          <strong id="tuto-step1-title">Zoomer & Déplacer</strong>
          <small id="tuto-step1-desc">Pincez avec 2 doigts ou utilisez la molette de la souris pour naviguer sur la carte.</small>
        </div>
      </div>
      
      <!-- Step 2 -->
      <div class="opt-btn" style="cursor: default; pointer-events: none;">
        <span class="opt-dot" style="display: flex; align-items: center; justify-content: center; background: #e5e7eb; border: none; font-size: 0.8rem; width: 24px; height: 24px; color: #111111;"><i class="fa-solid fa-location-dot"></i></span>
        <div>
          <strong id="tuto-step2-title">Sélectionner un Statut</strong>
          <small id="tuto-step2-desc">Cliquez sur une région ou un département pour enregistrer votre niveau d'exploration.</small>
        </div>
      </div>
      
      <!-- Step 3 -->
      <div class="opt-btn" style="cursor: default; pointer-events: none;">
        <span class="opt-dot" style="display: flex; align-items: center; justify-content: center; background: #e5e7eb; border: none; font-size: 0.8rem; width: 24px; height: 24px; color: #111111;"><i class="fa-solid fa-share-nodes"></i></span>
        <div>
          <strong id="tuto-step3-title">Exporter & Partager</strong>
          <small id="tuto-step3-desc">Cliquez sur le bouton d'export pour télécharger une superbe carte prête pour vos réseaux sociaux !</small>
        </div>
      </div>
    </div>
    
    <div style="padding: 20px 16px;">
      <button id="btn-tuto-close" style="width: 100%; border: 1.5px solid #111111; background: #111111; color: #ffffff; border-radius: 0; padding: 14px; font-size: 0.9rem; font-weight: 900; text-transform: uppercase; font-family: var(--font); cursor: pointer; transition: all 0.15s ease;">C'est parti !</button>
    </div>
  </div>
</div>"""

    if old_tutorial_html in content_html:
        content_html = content_html.replace(old_tutorial_html, new_tutorial_html)
        print("Success: index.html tutorial HTML updated!")
    else:
        # Fallback split
        print("Warning: index.html tutorial modal exact string not found. Trying block replace.")
        idx_start = content_html.find('<!-- ═══════════════════════════════════════════ TUTORIAL POPUP MODAL -->')
        idx_end = content_html.find('<!-- ═══════════════════════════════════════════ TOAST -->')
        if idx_start != -1 and idx_end != -1:
            old_block = content_html[idx_start:idx_end]
            content_html = content_html.replace(old_block, new_tutorial_html + "\n\n")
            print("Success: index.html tutorial HTML updated via block replace!")
        else:
            print("Error: Could not locate tutorial block in index.html")

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content_html)

    # ─── PART 2: Update update_app.py ───────────────────────────
    with open("update_app.py", "r", encoding="utf-8") as f:
        content_app = f.read()

    # Find DOMContentLoaded tutorial loader block
    old_loader_block = """  // Show tutorial modal on load
  const tutoOverlay = document.getElementById("tutorial-overlay");
  if (tutoOverlay) {
    tutoOverlay.classList.remove("hidden");
    const closeBtn = document.getElementById("btn-tuto-close");
    if (closeBtn) {
      closeBtn.addEventListener("click", () => {
        tutoOverlay.classList.add("hidden");
      });
    }
  }"""

    new_loader_block = """  // Show tutorial modal on load
  const tutoOverlay = document.getElementById("tutorial-overlay");
  if (tutoOverlay) {
    tutoOverlay.classList.remove("hidden");
    
    const closeTuto = () => {
      tutoOverlay.classList.add("hidden");
    };
    
    const closeBtn = document.getElementById("btn-tuto-close");
    if (closeBtn) closeBtn.addEventListener("click", closeTuto);
    
    const headerCloseBtn = document.getElementById("btn-tuto-header-close");
    if (headerCloseBtn) headerCloseBtn.addEventListener("click", closeTuto);
  }"""

    if old_loader_block in content_app:
        content_app = content_app.replace(old_loader_block, new_loader_block)
        print("Success: update_app.py DOMContentLoaded loader updated!")
    else:
        print("Error: Could not find old loader block in update_app.py")

    with open("update_app.py", "w", encoding="utf-8") as f:
        f.write(content_app)

    # ─── PART 3: Update styles.css ──────────────────────────────
    with open("styles.css", "r", encoding="utf-8") as f:
        content_css = f.read()

    # We want to remove all the redundant tutorial classes at the end of styles.css
    # Let's search for `#tutorial-modal {` and delete everything from there to the end
    idx_tuto_style = content_css.find("#tutorial-modal {")
    if idx_tuto_style != -1:
        # Delete everything after "#tutorial-modal {" but keep our new button hover transition style!
        content_css = content_css[:idx_tuto_style]
        # Append beautiful button hover transition
        content_css += """#btn-tuto-close:hover {
  background: #222222 !important;
  transform: translateY(-1px);
}
"""
        print("Success: styles.css redundant custom classes cleaned up and matched!")
    else:
        print("Warning: tutorial-modal styles not found at end of styles.css")

    with open("styles.css", "w", encoding="utf-8") as f:
        f.write(content_css)

if __name__ == "__main__":
    main()
