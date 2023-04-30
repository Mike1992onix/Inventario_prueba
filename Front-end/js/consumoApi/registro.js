formulario = document.getElementById('form_registro');
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
      window.location.href = 'login.html';
    }, 3000);
  }

let btn_registro = document.getElementById('registro_btn');
btn_registro.addEventListener('click', async (event) => {
    event.preventDefault();
    var datos = new FormData(formulario);

    const options = {
        method: 'POST',
        body: JSON.stringify({
            Documento:datos.get('documento'),
            Nombre:datos.get('nombre'),
            usuario: datos.get('usuario'),
            contraseña:datos.get('password'),
            email: datos.get('email'),
            Observaciones: datos.get('observaciones')
        }),
        headers: {
            'Content-Type': 'application/json'
        }
      };
      
    const response = await fetch("http://127.0.0.1:5000/registro", options);
    if(response.status === 204){
        console.log('se registro correctamente');
        redireccionar();
    }else{
        console.log('hubo error');
    }
});