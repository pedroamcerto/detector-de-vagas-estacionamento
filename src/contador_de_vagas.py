import cv2 as cv
import numpy as np
import json

def carregar_configuracao(nome_arquivo):
    try:
        with open(nome_arquivo) as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo JSON: '{nome_arquivo}'.")
    return None

def detectar_vagas_estacionamento(frame, config, vagas):
    #Manipula a imagem
    cinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(cinza, (3, 3), 1)
    th = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 25, 16)
    kernel = np.ones((3, 3), np.uint8())
    opening = cv.morphologyEx(th, cv.MORPH_OPEN, kernel)
    median = cv.medianBlur(opening, 5)
    dilatada = cv.dilate(median, kernel, iterations=1)

    # Verifica se o usuário deseja ver a visão binária
    if config['visao']['mostrar_binaria']:
        cv.imshow("Binary Vision", dilatada)

    qtyVagasUtilizadas = 0  # Variável que armazena a quantidade de vagas utilizadas
    for vaga in vagas:
        # Realiza o recorte no retângulo da vaga
        recorte = dilatada[vaga['y']:vaga['y'] + vaga['h'], vaga['x']:vaga['x'] + vaga['w']]
        # Analisa a quantidade de pixels brancos na imagem binária
        qtyPixelsBrancos = cv.countNonZero(recorte)

        bgr = config['cores']['vaga_livre']
        # Verifica se a vaga está sendo utilizada
        if qtyPixelsBrancos > config['max_pixels_brancos']:
            bgr = config['cores']['vaga_utilizada']
            qtyVagasUtilizadas += 1

        # Verifica se o usuário deseja ver a quantidade de pixels brancos
        if config['visao']['mostrar_qtd_pixels_brancos']:
            # Insere o texto mostrando a quantidade de pixels brancos detectados
            cv.putText(frame, str(qtyPixelsBrancos), (vaga['x'] + 10, vaga['y'] + 20), cv.FONT_ITALIC, 0.7,
                       config['cores']['txt_qtd_pixels_brancos'], 1)
        if config['visao']['mostrar_retangulo']:
            # Insere o retângulo na imagem, que cerca cada vaga
            cv.rectangle(frame, (vaga['x'], vaga['y']), (vaga['x'] + vaga['w'], vaga['y'] + vaga['h']), bgr, config['visao']['espessura_do_retangulo'])

    return frame, qtyVagasUtilizadas

def main():
    # Carregar configurações
    config = carregar_configuracao("config/config.json")
    vagas = carregar_configuracao("config/vagas_config.json")

    if config is None or vagas is None:
        return

    # Abrir vídeo
    video = cv.VideoCapture(filename="video/video.mp4")
    if not video.isOpened():
        print('Não foi possível abrir o vídeo.')
        return

    while True:
        # Ler frame do vídeo
        ret, frame = video.read()
        if not ret:
            break

        # Detectar vagas de estacionamento
        frame, qtde_vagas_utilizadas = detectar_vagas_estacionamento(frame, config, vagas)

        if config['visao']['mostrar_titulo']:
            h = frame.shape[0]  # Altura da imagem
            # Insere o texto da quantidade de vagas utilizadas/total de vagas
            cv.putText(img=frame, text=f'Vagas utilizadas: {qtde_vagas_utilizadas} / {len(vagas)}', org=(10, h - 15),
                       fontFace=cv.FONT_ITALIC, fontScale=1, color=config['cores']['titulo'], thickness=2, )
        # Mostrar frame
        cv.imshow("Camera 01", frame)

        if cv.waitKey(15) & 0xFF == ord('q'):
            break

    video.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
