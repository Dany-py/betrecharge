
const mon= document.querySelector('#amount')

let amount= parseInt(mon, 10)+ (parseInt(mon, 10)*0.06)

const btn=document.querySelector('.button-class')

btn.setAttribute("data-transaction-amount", amount)
