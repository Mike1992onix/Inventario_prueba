let categoria_btn = document.getElementById('categoria_btn');
let productos_btn = document.getElementById('productos_btn');
let categorias = document.getElementById('categorias');
let productos = document.getElementById('productos');

categoria_btn.addEventListener('click', function(){
    productos.style.display = 'none';
    categorias.style.display = 'block';
});

productos_btn.addEventListener('click', function(){
    categorias.style.display = 'none';
    productos.style.display = 'block';
});