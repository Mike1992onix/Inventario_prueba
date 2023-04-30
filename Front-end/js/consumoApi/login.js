formulario = document.getElementById('login_form');
const Constants = {
    MAIN_URL: 'http://localhost:5000',
    LOGIN : '/login',
    REGISTRO_USUARIO: '/registro',
    CREAR_ELEMENTO: '/elements/create',
    CREAR_CATEGORIA: '/category/create',
    MODIFICAR_ELEMENTO: '/elements/update',
    MODIFICAR_CATEGORIA: '/category/update',
    ELIMINAR_ELEMENTO: '/elements/delete',
    ELIMINAR_CATEGORIA: '/category/delete',
    CONSULTAR_ELEMENTO: '/elements/read',
    CONSULTAR_CATEGORIA: '/elements/read' 
}
function redireccionar() {
    setTimeout(function () {
      window.location.href = 'index.html';
    }, 3000);
  }
let btn_login = document.getElementById('login_btn');
btn_login.addEventListener('click', async (event) => {
    event.preventDefault();
    var datos = new FormData(formulario);

    const options = {
        method: 'POST',
        body: JSON.stringify({
            usuario: datos.get('usuario') ,
            contraseña: datos.get('password')
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    };
    const response = await fetch(Constants.MAIN_URL + Constants.LOGIN, options);
    if(response.status === 200){
        redireccionar();
    }else{

    }
});
