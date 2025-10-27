from playwright.sync_api import Page, expect

import pytest

def test_check_box(page: Page):
    page.goto("https://demoqa.com/")

    # Navegar a la página de checkbox
    page.get_by_text("Elements").click()
    page.get_by_text("Check Box").click()

    # Esperar a que el árbol se cargue
    page.wait_for_selector(".rct-node")

    # Expande el árbol principal (el botón de "Toggle" junto a "Home")
    page.locator(".rct-icon-expand-close").click()

    # Haz clic en el checkbox de 'Desktop'
    page.locator('label[for="tree-node-desktop"]').click()

    # Verifica que el checkbox esté marcado
    checkbox = page.locator('#tree-node-desktop')
    expect(checkbox).to_be_checked()

    # Haz clic en un nodo anidado, por ejemplo “Documents”
    page.locator('label[for="tree-node-documents"]').click()
    expect(page.locator('#tree-node-documents')).to_be_checked()

    # Esperar que el resultado aparezca
    result = page.locator("#result")
    expect(result).to_be_visible()

    # Verificar que el texto del resultado contenga las selecciones
    expect(result).to_contain_text("You have selected :")
    expect(result).to_contain_text("desktop")
    expect(result).to_contain_text("documents")

    page.pause()


