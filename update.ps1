$files = Get-ChildItem -Path . -Filter *.html
foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw

    if ($content -notmatch 'app\.js') {
        $content = $content -replace '</head>', "    <script src="app.js" defer></script>
</head>"
    }

    if ($content -notmatch 'michelle_aquino_psicologia8') {
        $content = $content -replace '(<a href="https://wa\.me/5521986583952" target="_blank">WhatsApp</a>)', "$1
                    <a href="https://www.instagram.com/michelle_aquino_psicologia8/" target="_blank">Instagram</a>"
    }

    if ($content -notmatch 'btn-mobile-menu') {
        $burgerBtn = "
            <button class="btn-mobile-menu" aria-label="Menu">" +
                     "
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>" +
                     "
            </button>"
        $content = $content -replace '(<div class="nav-cta">[\s\S]*?</div>)', "$1$burgerBtn"
    }

    if ($content -notmatch 'btn-close-menu') {
        $closeBtn = "
                <button class="btn-close-menu" aria-label="Fechar">" +
                    "
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>" +
                    "
                </button>"
        $content = $content -replace '(<ul class="nav-list">)', "$closeBtn
                $1"
    }

    Set-Content -Path $file.FullName -Value $content -Encoding UTF8
}
