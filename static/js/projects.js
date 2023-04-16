let webProjectsBtn = document.getElementById('btnWeb');
let androidProjectsBtn = document.getElementById('btnAndroid');

let webProjectsContainer = document.getElementById('web');
let androidProjectsContainer = document.getElementById('android');


webProjectsBtn.addEventListener('click', ()=>{

    androidProjectsBtn.classList.remove('tab-active');
    webProjectsBtn.classList.add('tab-active');

    webProjectsContainer.classList.toggle('hide');
    androidProjectsContainer.classList.toggle('hide');

});
androidProjectsBtn.addEventListener('click', ()=>{

    androidProjectsBtn.classList.add('tab-active');
    webProjectsBtn.classList.remove('tab-active');
    webProjectsContainer.classList.toggle('hide');
    androidProjectsContainer.classList.toggle('hide');

});