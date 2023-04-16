let btnWebSkill = document.getElementById('btnWebSkill');
let btnAndroidSkill = document.getElementById('btnAndroidSkill');

let webSkill = document.getElementById('webSkill');
let mobileSkill = document.getElementById('mobileSkill');


btnWebSkill.addEventListener('click', ()=>{

    btnAndroidSkill.classList.remove('tab-active');
    btnWebSkill.classList.add('tab-active');

    webSkill.classList.toggle('hide');
    mobileSkill.classList.toggle('hide');

});
btnAndroidSkill.addEventListener('click', ()=>{

    btnAndroidSkill.classList.add('tab-active');
    btnWebSkill.classList.remove('tab-active');
    webSkill.classList.toggle('hide');
    mobileSkill.classList.toggle('hide');

});