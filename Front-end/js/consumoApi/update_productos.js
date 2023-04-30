let formulario = document.getElementById('form_productos');
let btn = document.getElementById('guardar-producto');


btn.addEventListener('click', async(event) =>{
    event.preventDefault();
    var datos = new FormData(formulario);

const options = {
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    ID_elemento: datos.get('id'),
    referencia : datos.get('referencia'),
    nombres : datos.get('nombres'),
    cantidad: datos.get('cantidad'),
    valor : datos.get('valor'),
    estado : datos.get('estado'),
    lugar: datos.get('lugar'),
    Observaciones: datos.get('lugar'),
    ID_categoria: datos.get('categoria'),
  }),
};

const response = await fetch('http://localhost:5000/elements/update', options);


      if(response.status === 200){
        alert('producto creado exitosamente');
      }else{
        alert('error');
      }

});