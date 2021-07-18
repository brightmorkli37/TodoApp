const btn = document.querySelector('button')

btn.onmouseover = () => {
    btn.style.backgroundColor = 'cyan';
    setTimeout(() => btn.style.backgroundColor = 'black', 2000);
}
