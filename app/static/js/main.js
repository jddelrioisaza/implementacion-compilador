
document.getElementById("CompilarButton").addEventListener("click", function() {
    var messageElement = document.createElement("div");
    messageElement.innerHTML = "Compilando...";
    messageElement.classList.add("Mensaje");
    document.body.appendChild(messageElement);
  
    setTimeout(function() {
      document.body.removeChild(messageElement);
    }, 3000); // Elimina el mensaje después de 3 segundos (3000 ms)
  });

// Configuración de i18next
i18next.init({
    lng: 'es', // Idioma predeterminado
    resources: {
      en: {
        translation: {
          compile: 'Compile',
          execute: 'Execute',
          placeholder: 'Write your code here',
          english: 'English',
          spanish: 'Spanish',
          french: 'French',
        }
      },
      es: {
        translation: {
          compile: 'Compilar',
          execute: 'Ejecutar',
          placeholder: 'Escribe tu código aquí',
          english: 'Inglés',
          spanish: 'Español',
          french: 'Francés',
        }
      },
      fr: {
        translation: {
          compile: 'Compiler',
          execute: 'Exécuter',
          placeholder: 'Écrivez votre code ici',
          english: 'Anglais',
          spanish: 'Espagnol',
          french: 'Français',
        }
      }
    }
  }, function(err, t) {
    // Aplicar las traducciones a los elementos de la página
    document.getElementById('CompilarButton').textContent = t('compile');
    document.getElementById('EjecutarButton').textContent = t('execute');
    document.getElementById('SpanishButton').textContent = t('spanish');
    document.getElementById('EnglishButton').textContent = t('english');
    document.getElementById('FrenchButton').textContent = t('french');
    document.getElementById('TextoIngresado').setAttribute('placeholder', t('placeholder'));
  
    // Agregar eventos de clic a los botones de idioma
    document.getElementById('EnglishButton').addEventListener('click', function() {
      i18next.changeLanguage('en', function(err, t) {
        if (err) return console.log('Error al cambiar el idioma: ', err);
        applyTranslations(t);
      });
    });
  
    document.getElementById('SpanishButton').addEventListener('click', function() {
      i18next.changeLanguage('es', function(err, t) {
        if (err) return console.log('Error al cambiar el idioma: ', err);
        applyTranslations(t);
      });
    });
  
    document.getElementById('FrenchButton').addEventListener('click', function() {
      i18next.changeLanguage('fr', function(err, t) {
        if (err) return console.log('Error al cambiar el idioma: ', err);
        applyTranslations(t);
      });
    });
  
    function applyTranslations(t) {
      document.getElementById('CompilarButton').textContent = t('compile');
      document.getElementById('EjecutarButton').textContent = t('execute');
      document.getElementById('SpanishButton').textContent = t('spanish');
      document.getElementById('EnglishButton').textContent = t('english');
      document.getElementById('FrenchButton').textContent = t('french');
      document.getElementById('TextoIngresado').setAttribute('placeholder', t('placeholder'));
    }
  });