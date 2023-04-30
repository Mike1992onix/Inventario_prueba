// se instancia una variable con el id del boton del html 
let btn_crear_categoria = document.getElementById('enviar');
let formulario = document.getElementById('form_creacion');

btn_crear_categoria.addEventListener('click', async(event) => {
    //evita que la pagina se recarge
    event.preventDefault();
    // traer la data del formulario 
    var datos = new FormData(formulario);

    //simula el json que envia en el postman, si no se requiere no se envia o se puede enviar los datos por la url en metodos DELETE Y GET
    const options = {
        method: 'POST',
        body: JSON.stringify({
            codigo : datos.get('codigo'),
            nombre : datos.get('nombre'),
            descripcion: datos.get('descripcion'),
            observacion : datos.get('observacion')
        }),
        headers: {
            'Content-Type': 'application/json'
        }
      };
    
      const response = await fetch('http://localhost:5000/category/create', options);

      if(response.status === 201){
        console.log('usuario creado exitosamente');
      }else{
        console.log('error');
      }

});