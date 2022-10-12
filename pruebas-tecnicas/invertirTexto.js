const invertirTexto = (text) => {
  let result = "";
  for (let i = 1; i <= text.length; i++) {
    result = result + text[text.length - i];
  }
  return result;
};

const texto = "Este es un texto de prueba.";

console.log(invertirTexto(texto));
