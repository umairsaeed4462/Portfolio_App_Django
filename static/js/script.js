// ================ tying Animation =================

let typed = new Typed('.typing',{
    strings: [" ","Full Stack Developer", "Graphics Designer", "Python Developer", "Mobile App Developer"],
    typeSpeed: 100,
    BackSpeed: 60,
    loop:true
})


// ============== working on toggle ==============

let clossToggle = document.getElementById('clossTogal');
let toggle = document.getElementById('simpleToggle');

let navbarBox = document.getElementById('navbar-section');
let mainSection = document.getElementById('main-section');

toggle.addEventListener('click', ()=>{
    navbarBox.classList.toggle('hidden');
    mainSection.classList.toggle('hidden');
});

clossToggle.addEventListener('click', ()=>{
    navbarBox.classList.toggle('hidden');
    mainSection.classList.toggle('hidden');
})


// ============== End working on toggle ============== 


// working on navbar items

let btnHome = document.getElementById('navBtnHome');
let btnAbout = document.getElementById('navBtnAbout');
let btnServices = document.getElementById('navBtnServices');
let btnProjects = document.getElementById('navBtnProjects');
let btnSkill = document.getElementById('navBtnSkill');
let btnContact = document.getElementById('navBtnContent');

let homeSection = document.getElementById('homeSection');
let contactSection = document.getElementById('contactSection');
let servicesSection = document.getElementById('servicesSection');
let aboutSection = document.getElementById('aboutSection');
let skillSection = document.getElementById('skillSection');
let projectSection = document.getElementById('projectSection');

btnHome.addEventListener('click', ()=>{
    clossAllSections();
    homeSection.classList.remove('hide');
});

btnAbout.addEventListener('click', ()=>{

    clossAllSections();
    navbarBox.classList.toggle('hidden');
    mainSection.classList.toggle('hidden');
    
    aboutSection.classList.remove('hide');
});
btnServices.addEventListener('click', ()=>{
    clossAllSections();
    servicesSection.classList.remove('hide');
});
btnContact.addEventListener('click', ()=>{
    clossAllSections();
    contactSection.classList.remove('hide');
});
btnSkill.addEventListener('click', ()=>{
    clossAllSections();
    skillSection.classList.remove('hide');
});
btnProjects.addEventListener('click', ()=>{
    clossAllSections();
    projectSection.classList.remove('hide');
});

function clossAllSections() {

    homeSection.classList.add('hide');
    aboutSection.classList.add('hide');
    contactSection.classList.add('hide');
    skillSection.classList.add('hide');
    servicesSection.classList.add('hide');
    projectSection.classList.add('hide');

    navbarBox.classList.toggle('hidden');
    mainSection.classList.toggle('hidden');

    if(document.getElementById("m1") != null){
        document.getElementById("m1").innerHTML = ""
    }
    if(document.getElementById("m2") != null){
        document.getElementById("m2").innerHTML = ""
    }



}