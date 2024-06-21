// function dias_mes(mes, ano) {
//     ano = ano || new Date().getFullYear()
//     return new Date(ano, mes, 0).getDate()
// }

// const meses = {
//     'janeiro': 0, 'fevereiro': 1, 'março': 2, 'abril': 3,
//     'maio': 4, 'junho': 5, 'julho': 6, 'agosto': 7,
//     'setembro': 8, 'outubro': 9, 'novembro': 10, 'dezembro': 11
// }

// let mes = 'fevereiro'
// let ano = 2024
// let numeroMes == meses[mes.toLowerCase()]

// if (numeroMes !== undefined) {
//     let dias = dias_mes(numeroMes + 1, ano)
//     console.log(`O mês ${mes} tem ${dias} dias.`);
// } else {
//     // console.log(`Mês inválido: ${mes}`)
// }

mes = "junho"

if(mes == "janeiro" || mes == "março"|| mes == "maio"|| mes == "julho"|| mes == "agosto"|| mes == "outubro"||mes == "dezembro"){
    console.log("O mês de " + mes + " tem 31 dias")
} 
else if (mes == "abril"|| mes == "junho"|| mes == "setembro"|| mes == "novembro"){
    console.log("O mês de " + mes + " tem 30 dias")
} 
else if (mes == "fevereiro"){
    console.log("O mês de "+ mes + " tem 28 dias")
}