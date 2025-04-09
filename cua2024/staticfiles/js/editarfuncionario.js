function editarFuncionario(id) {
    fetch(`/editar_funcionario/${id}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}', // Asegúrate de que el token CSRF esté disponible
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            // Agrega aquí los datos que necesites enviar, si corresponde
        })
    })
    .then(response => {
        if (response.ok) {
            // Maneja la respuesta
            window.location.reload(); // o redirige a otra página si es necesario
        } else {
            // Maneja el error
            console.error('Error al editar:', response.statusText);
        }
    });
}