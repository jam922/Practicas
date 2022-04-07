function getSistemaOperativo() {
    let disp=document.getElementsByName('dispositivo');
    let IOS= disp[0];
    let ANDROID = disp[1];
    var userAgent = navigator.userAgent || navigator.vendor || window.opera;
    
    if (/android/i.test(userAgent) && !window.MSStream) {
        console.log('Android')
        IOS.classList.replace('active','disabled')
        if (ANDROID.classList.contains('disabled')) {
            ANDROID.classList.replace('disabled','active')
        }
    }
  
    if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
        console.log('iOS')
        ANDROID.classList.replace('active','disabled')
        if (IOS.classList.contains('disabled')) {
            IOS.classList.replace('disabled','active')
        }
    }
    
    if(!/android/i.test(userAgent) && !/iPad|iPhone|iPod/.test(userAgent)){
        console.log('desconocido')
        if(ANDROID.classList.contains('disabled') || IOS.classList.contains('disabled')){
            ANDROID.classList.replace('disabled','active')
            IOS.classList.replace('disabled','active')
        }
    }
}

setInterval('getSistemaOperativo()',1000)