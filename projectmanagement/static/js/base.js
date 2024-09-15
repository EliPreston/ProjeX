// document.addEventListener("DOMContentLoaded", () => {


//     // Mobile menu toggle
//     const mobileMenuButton = document.getElementById('mobile-menu-button')
//     const mobileMenu = document.getElementById('mobile-menu')    
//     mobileMenuButton.addEventListener('click', () => {
//       // if mobileMenu.classList.contains(class);
//       mobileMenu.classList.toggle('hidden')
//     })

    
//     const profileMenuButton = document.getElementById('profile-menu-button')
//     const profileMenu = document.getElementById('profile-menu')
//     profileMenuButton.addEventListener('click', () => {
//       profileMenu.classList.toggle('hidden')
//     })
    
    
//   })
  


document.addEventListener("DOMContentLoaded", () => {


  // Mobile menu toggle
  const mobileMenuButton = document.getElementById('mobile-menu-button')
  const mainMenu = document.getElementById('mainMenu')    
  mobileMenuButton.addEventListener('click', () => {
      mainMenu.classList.toggle('hidden')
  })


  const profileMenuButton = document.getElementById('profile-menu-button')
  const profileMenu = document.getElementById('profile-menu')
  profileMenuButton.addEventListener('click', () => {
      profileMenu.classList.toggle('hidden')
  })
})   