from playwright.sync_api import Page, expect
from faker import Faker
fake = Faker()

def test_text_box(page: Page):
    page.goto("https://demoqa.com/")

    # Navegar hasta Text Box
    page.get_by_text("Elements").click()
    page.get_by_text("Text Box").click()

    # Generar datos solo una vez
    name = fake.name()
    email = fake.email()
    current_address = fake.address().replace("\n", " ")
    permanent_address = fake.address().replace("\n", " ")

    # Llenar el formulario
    page.locator("#userName").fill(name)
    page.locator("#userEmail").fill(email)
    page.locator("#currentAddress").fill(current_address)
    page.locator("#permanentAddress").fill(permanent_address)

    # Enviar el formulario
    page.locator("#submit").click()

    # Esperar que el output sea visible
    output = page.locator("#output")
    expect(output).to_be_visible()

    # ✅ Validar dentro del contenedor del output
    expect(output.locator("#name")).to_have_text(f"Name:{name}")
    expect(output.locator("#email")).to_have_text(f"Email:{email}")
    expect(output.locator("#currentAddress")).to_have_text(f"Current Address :{current_address}")
    expect(output.locator("#permanentAddress")).to_have_text(f"Permananet Address :{permanent_address}")

    # Pausa opcional para inspeccionar la ejecución
    page.pause()
