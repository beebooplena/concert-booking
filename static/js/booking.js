// let btnplus = document.querySelector('.plus');
// let btnminus = document.querySelector('.minus');

// let quantity = document.querySelector('#totalClicks');
// let hiddenInput = document.getElementById("hiddenInput");



// btnplus.addEventListener('click', ()=>{
//         const currentValue = +hiddenInput.value;
//         if(currentValue > 3){
//             return
//         }
//         quantity.innerText = currentValue + 1;
//         hiddenInput.value = currentValue + 1;
       
        
//     })


// btnminus.addEventListener('click', ()=>{
//     const currentValue = +hiddenInput.value;
//     if(currentValue==0)return
    
//     quantity.innerText = currentValue - 1;
//     hiddenInput.value = currentValue - 1;
// })

let test = document.getElementById('#id_order');
let ja = document.getElementsByName('order')

test.addEventListener('click', ()=>{
    const hello = test.ariaValueMax;
    console.log("hello")
    if (hello > 3){
        return
    }
})
ja.addEventListener('click', ()=>{
    const hello = test.value;
    console.log("hello")
    if (hello > 3){
        return
    }
})


