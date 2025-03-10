import pandas as pd
from etl import Etl

def main():
    LINKS = [
        "https://www.argenprop.com/departamento-en-alquiler-en-villa-pueyrredon-2-ambientes--17065744",
        "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-departamento-villa-urquiza-55708519.html",
        "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-monoambiente-en-alquiler-al-frente-42561207.html",
        "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-sanabria-2100-departamento-1-ambiente-c-balcon-55501405.html",
        "https://www.zonaprop.com.ar/propiedades/clasificado/alclappa-excelente-ubicacion-monoambiente-luminoso!-55463946.html",
        "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-compacto-2-ambientes-en-el-corazon-de-chacarita-55427393.html",
        "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-monoambiente-alquiler-con-balcon-a-estrenar-55641827.html",
        "https://www.zonaprop.com.ar/propiedades/clasificado/alclapin-alquiler-monoambiente-con-balcon-villa-pueyrredon-55666582.html",

    ]

    data_list = Etl(LINKS).get_data()


    df = pd.DataFrame(data_list)

    print(df)
    return df

if __name__ == "__main__":
    main()