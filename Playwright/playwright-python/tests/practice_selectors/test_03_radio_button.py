from playwright.sync_api import Page, expect

def test_check_box(page: Page):
    page.goto("https://demoqa.com/")

    # Navegar a la página de Radio Button
    page.get_by_text("Elements").click()
    page.get_by_text("Radio Button").click()

    # Hacer clic sobre el label visible (no el input)
    page.locator("label[for='yesRadio']").click()
    expect(page.locator("#yesRadio")).to_be_checked()

    # Verificar que el radio se activó correctamente
    result = page.locator(".mt-3")
    expect(result).to_contain_text("You have selected ")
    expect(result).to_contain_text("Yes")

    # Hacer clic sobre el label visible (no el input)
    page.locator("label[for='impressiveRadio']").click()
    expect(page.locator("#impressiveRadio")).to_be_checked()

    # Verificar que el radio se activó correctamente
    result = page.locator(".mt-3")
    expect(result).to_contain_text("You have selected ")
    expect(result).to_contain_text("Impressive")

    expect(page.locator("#noRadio")).to_be_disabled()

    page.pause()


