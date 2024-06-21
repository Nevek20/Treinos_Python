peso = 70
altura = 1.70
calAlt = altura * altura
var imc = peso / calAlt

console.log("Seu IMC é " + imc)

if(imc<18.5){
    console.log("Abaixo do peso")
}else if (imc>=18.5 && imc <25){
    console.log("Peso comum")
}else if (imc>=25 && imc <32){
    console.log("Acima do peso")
}
