# Selenium + Java Cheat Sheet

Guía rápida de comandos y snippets útiles con **Selenium WebDriver en Java**.  

## 📑 Índice
1. [🚀 Configuración Básica](#🚀-configuración-básica)
2. [🔍 Localizadores](#🔍-localizadores)
3. [⌨️ Acciones Comunes](#⌨️-acciones-comunes)
4. [🕒 Esperas](#🕒-esperas)
5. [🌍 Navegación](#🌍-navegación)
6. [📦 Manejo de Elementos Avanzados](#📦-manejo-de-elementos-avanzados)  
   - [Dropdowns](#dropdowns)  
   - [Alertas](#alertas)  
   - [iFrames](#iframes)
7. [🖱️ Acciones con el Mouse y Teclado](#🖱️-acciones-con-el-mouse-y-teclado)
8. [📸 Screenshots](#📸-screenshots)
9. [🔄 Ejecución en Diferentes Navegadores](#🔄-ejecución-en-diferentes-navegadores)

## 🚀 Configuración Básica

```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import io.github.bonigarcia.wdm.WebDriverManager;

public class Main {
    public static void main(String[] args) {
        // Configura automáticamente ChromeDriver
        WebDriverManager.chromedriver().setup();

        // Inicializa el navegador
        WebDriver driver = new ChromeDriver();

        // Navega a una página web
        driver.get("https://demoqa.com/text-box");

        // Maximizar ventana
        driver.manage().window().maximize();

        // Imprime el título de la página
        System.out.println("Título de la página: " + driver.getTitle());

        // Cierra el navegador
        driver.quit();
    }
}
```

## 🔍 Localizadores

```Java
driver.findElement(By.id("id"));
driver.findElement(By.name("nombre"));
driver.findElement(By.className("clase"));
driver.findElement(By.tagName("input"));
driver.findElement(By.linkText("TextoLink"));
driver.findElement(By.partialLinkText("TextoParcial"));
driver.findElement(By.cssSelector("input[type='text']"));
driver.findElement(By.xpath("//div[@class='clase']"));
```

## ⌨️ Acciones Comunes

```Java
WebElement input = driver.findElement(By.id("username"));

// Escribir texto
input.sendKeys("miUsuario");

// Limpiar campo
input.clear();

// Click
driver.findElement(By.id("login")).click();

// Obtener texto
String texto = driver.findElement(By.id("mensaje")).getText();

// Obtener atributo
String valor = input.getAttribute("value");
```

## 🕒 Esperas

### Implícitas

```Java
driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
```

### Explícitas

```Java
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
WebElement element = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("username")));
```

## 🌍 Navegación

```Java
driver.navigate().to("https://example.com");
driver.navigate().back();
driver.navigate().forward();
driver.navigate().refresh();
```

## 📦 Manejo de Elementos Avanzados

### Dropdowns

```Java
Select dropdown = new Select(driver.findElement(By.id("pais")));
dropdown.selectByVisibleText("Ecuador");
dropdown.selectByValue("EC");
dropdown.selectByIndex(2);
```

### Alertas

```Java
Alert alert = driver.switchTo().alert();
alert.accept();  // OK
alert.dismiss(); // Cancelar
alert.sendKeys("Texto"); // Escribir en alerta
```

### iFrames

```Java
driver.switchTo().frame("frameName");
// volver al DOM principal
driver.switchTo().defaultContent();
```

## 🖱️ Acciones con el Mouse y Teclado

```Java
Actions actions = new Actions(driver);

// Hover
actions.moveToElement(driver.findElement(By.id("menu"))).perform();

// Drag and Drop
WebElement source = driver.findElement(By.id("origen"));
WebElement target = driver.findElement(By.id("destino"));
actions.dragAndDrop(source, target).perform();

// Teclado
actions.sendKeys(Keys.ENTER).perform();
```

## 📸 Screenshots

```Java
File screenshot = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
FileUtils.copyFile(screenshot, new File("captura.png"));
```

## 🔄 Ejecución en Diferentes Navegadores

```Java
WebDriver driver = new FirefoxDriver();
WebDriver driver = new EdgeDriver();
```