let burger = document.querySelector('.burger');
let navbar = document.querySelector('.navbar');
let navList = document.querySelector('.nav-list');
let btn = document.querySelector('.btn');
let quizdiv = document.getElementById('quiz-btn');

burger.addEventListener('click', ()=>{
    
    navList.classList.toggle('v-class-resp');
    navbar.classList.toggle('h-nav-resp');
})

btn.addEventListener('click', ()=>{
  quizdiv.innerHTML= '<iframe src="https://take.quiz-maker.com/QLDVMYO7J" width="90%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>'
  
})
