# Detector de Vagas de Estacionamento

Este projeto é um sistema de detecção de vagas de estacionamento em vídeos utilizando a biblioteca OpenCV em Python. Ele permite identificar vagas livres e ocupadas em um vídeo simulando uma câmera de vigilância.

## Funcionalidades

- Detecta e destaca as vagas de estacionamento em um vídeo.
- Conta o número de vagas livres e ocupadas.
- Mostra a visão binária e o número de pixels brancos em cada vaga.
- Configurações personalizáveis via arquivos JSON.

## Como usar

1. Clone este repositório para o seu computador:
```
git clone https://github.com/pedroamcerto/contador-de-vagas-opencv.git
```
2. Instale as dependências:
```
pip install -r requirements.txt
```
3. Configure os arquivos JSON conforme necessário:
   
   - `config.json`: configurações gerais do projeto.
   - `vagas_config.json`: configurações das vagas de estacionamento.

4. Execute o script principal:
```
python src/contador_de_vagas.py
```
5. Pressione 'q' para sair da aplicação.


## Configuração de visualização, cores e detecção

Para configurar as opções de visualização, cores e detecção do projeto, siga estas etapas:

1. Abra o arquivo `config.json` localizado na pasta `config` do seu projeto.

2. Dentro do arquivo `config.json`, você encontrará as seguintes seções:

```json
{
    "visao" :{
        "mostrar_binaria": false,
        "mostrar_qtd_pixels_brancos": false,
        "mostrar_titulo": true,
        "mostrar_retangulo": true,
        "espessura_do_retangulo": 1
    },
    "cores": {
        "titulo": [0, 0, 0],
        "vaga_livre": [0, 255, 0],
        "vaga_utilizada": [0, 0, 255],
        "txt_qtd_pixels_brancos": [255, 255, 255]
    },
    "max_pixels_brancos": 3000
}
```

1. Para alterar as configurações de visualização, defina os valores booleanos para true ou false, dependendo se deseja mostrar ou ocultar determinados elementos na tela.

2. Você também pode ajustar as cores alterando os valores BGR (Blue, Green, Red) fornecidos em cada chave dentro da seção cores.

3. Salve as alterações no arquivo config.json após fazer as mudanças desejadas.

4. Essas configurações afetam a aparência e o comportamento da aplicação durante a execução. Experimente diferentes combinações para atender às suas preferências e requisitos específicos.


## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE.md para mais detalhes.


