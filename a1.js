var par_impar = function(numero) {
    if (numero % 2 === 0) {
        return numero + " é par."
    } else {
        return numero + " é ímpar."
    }
}

console.log(par_impar(4))
console.log(par_impar(7))
