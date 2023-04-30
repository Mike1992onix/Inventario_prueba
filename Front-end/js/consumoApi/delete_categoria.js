const eliminar_categoria = async(id) => {
  const options = {method: 'DELETE'};
    
    const response = await fetch(`http://localhost:5000/category/delete/${id}`, options);

    if(response.status === 200){
      console.log('se elimino correctamente');
      location.reload();
    }else{
      console.log('hubo un problema');
    }
}
const eliminar_producto = async(id) => {
  const options = {method: 'DELETE'};
    
    const response = await fetch(`http://localhost:5000/elements/delete/${id}`, options);

    if(response.status === 200){
      console.log('se elimino correctamente');
      location.reload();
    }else{
      console.log('hubo un problema');
    }
}