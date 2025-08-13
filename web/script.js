document.getElementById('fichaForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const nome = document.getElementById('nome').value;
    const idade = document.getElementById('idade').value;
    const mutacao = document.getElementById('mutacao').value;
    const nivel = document.getElementById('nivel').value;

    const poderesSelect = document.getElementById('poder');
    const poderes = Array.from(poderesSelect.selectedOptions).map(option => option.value);

    const fichaDiv = document.getElementById('fichaExibida');
    fichaDiv.innerHTML = `
        <h2>Ficha de ${nome}</h2>
        <p><strong>Idade:</strong> ${idade}</p>
        <p><strong>Mutação:</strong> ${mutacao}</p>
        <p><strong>Nível:</strong> ${nivel}</p>
        <p><strong>Poderes:</strong></p>
        <ul>
            ${poderes.map(p => `<li>${p}</li>`).join('')}
        </ul>
    `;

    // Limpar o formulário (opcional)
    this.reset();
});