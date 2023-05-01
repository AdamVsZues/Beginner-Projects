const d = new Date();
document.getElementById("irldate").innerHTML = d.toDateString();


function calc() {
    let wage = document.getElementById('payrate').value;
    let hours = document.getElementById('hours').value;

    if (hours > 40){
    pay =(((parseInt(wage) * 10) * (parseInt(40) * 10))/100)
    overtimepay = (hours - 40) * (wage * 1.5)
    document.getElementById("grosspay").innerHTML = (' $' + (pay + overtimepay).toFixed(2))
    
    netpay =((((parseInt(wage) * 10) * (parseInt(40) * 10))/100 + overtimepay) - (((parseInt(wage) * 10) * (parseInt(hours) * 10)) / 100) *  (1/16)) - ((((parseInt(wage) * 10) * (parseInt(hours) * 10))/100) * (145/10000))
    document.getElementById("netpay").innerHTML = (' $' + netpay.toFixed(2))

    socialsecurity = ((((parseInt(wage) * 10) * (parseInt(hours) * 10))/100) - (((parseInt(wage) * 10) * (parseInt(hours) * 10))/100 - (((parseInt(wage) * 10) * (parseInt(hours) * 10)) / 100) *  (1/16)))
    document.getElementById("socials").innerHTML = (' -$' + socialsecurity.toFixed(2))

    medicare = ((((parseInt(wage) * 10) * (parseInt(hours) * 10))/100) - ((((parseInt(wage) * 10) * (parseInt(hours) * 10))/100) - ((((parseInt(wage) * 10) * (parseInt(hours) * 10))/100) * (145/10000))))
    document.getElementById("medicare").innerHTML = (' -$' + medicare.toFixed(2))
}
else {
    grosspay =(((parseInt(wage) * 10) * (parseInt(hours) * 10))/100)
    document.getElementById("grosspay").innerHTML = (' $' + grosspay.toFixed(2))
    
    netpay =(((parseInt(wage) * 10) * (parseInt(hours) * 10))/100 - (((parseInt(wage) * 10) * (parseInt(hours) * 10)) / 100) *  (1/16)) - ((((parseInt(wage) * 10) * (parseInt(hours) * 10))/100) * (145/10000))
    document.getElementById("netpay").innerHTML = (' $' + netpay.toFixed(2))

    socialsecurity = ((((parseInt(wage) * 10) * (parseInt(hours) * 10))/100) - (((parseInt(wage) * 10) * (parseInt(hours) * 10))/100 - (((parseInt(wage) * 10) * (parseInt(hours) * 10)) / 100) *  (1/16)))
    document.getElementById("socials").innerHTML = (' -$' + socialsecurity.toFixed(2))

    medicare = ((((parseInt(wage) * 10) * (parseInt(hours) * 10))/100) - ((((parseInt(wage) * 10) * (parseInt(hours) * 10))/100) - ((((parseInt(wage) * 10) * (parseInt(hours) * 10))/100) * (145/10000))))
    document.getElementById("medicare").innerHTML = (' -$' + medicare.toFixed(2))
}
}