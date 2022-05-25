let btnplus = document.querySelector('.plus');
let btnminus = document.querySelector('.minus');

let quantity = document.querySelector('#totalClicks');
let hiddenInput = document.getElementById("hiddenInput");



btnplus.addEventListener('click', ()=>{
        const currentValue = +hiddenInput.value;
        quantity.innerText = currentValue + 1;
        hiddenInput.value = currentValue + 1;
       
        
    })


btnminus.addEventListener('click', ()=>{
    const currentValue = +hiddenInput.value;
    if(currentValue==0)return
    
    quantity.innerText = currentValue - 1;
    hiddenInput.value = currentValue - 1;
})