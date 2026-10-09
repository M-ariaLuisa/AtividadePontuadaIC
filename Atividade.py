import customtkinter as ctk

ctk.set_appearance_mode('dark')



def calcular():
    try:
        n1 = float(nota1.get())
        n2 = float(nota2.get())

        media = (n1 + n2) / 2

        if media >= 7:
            resultado.configure(
                text=f'Situação: Aprovado!\nMédia: {media:.1f}',
                text_color='#2E7D32'
            )
        elif media >= 5:
            resultado.configure(
                text=f'Situação: Recuperação!\nMédia: {media:.1f}',
                text_color='#F57C00'
            )
        else:
            resultado.configure(
                text=f'Situação: Reprovado!\nMédia: {media:.1f}',
                text_color='#C62828'
            )
    except ValueError:
        resultado.configure(
            text='Digite apenas números válidos!',
            text_color='#C62828'
        )


janela = ctk.CTk()
janela.geometry('500x520')
janela.resizable(False, False)
janela.title('Resultado Acadêmico')
janela.configure(fg_color='#132233')
janela.iconbitmap('button_blank_blue_14984.ico')

subnome = ctk.CTkLabel(
    janela,
    text='Nome do aluno:',
    text_color='#fafbfc',
    font=('Arial', 18)
)
subnome.pack(pady=5)

nome = ctk.CTkEntry(
    janela,
    placeholder_text='Digite o nome do aluno',
    border_color='#09122e',
    text_color='#fafbfc',
    width=400,
    height=45,
    font=('Arial', 18)
)
nome.pack(pady=20)

subnota1 = ctk.CTkLabel(
    janela,
    text='Insira a nota 1:',
    text_color='#fafbfc',
    font=('Arial', 18)
)
subnota1.pack(pady=5)

nota1 = ctk.CTkEntry(
    janela,
    placeholder_text='Digite a nota 1',
    border_color='#09122e',
    text_color='#fafbfc',
    width=400,
    height=45,
    font=('Arial', 18)
)
nota1.pack(pady=8)

subnota2 = ctk.CTkLabel(
    janela,
    text='Insira a nota 2:',
    text_color='#fafbfc',
    font=('Arial', 18)
)
subnota2.pack(pady=5)

nota2 = ctk.CTkEntry(
    janela,
    placeholder_text='Digite a nota 2',
    border_color='#09122e',
    text_color='#fafbfc',
    width=400,
    height=45,
    font=('Arial', 18)
)
nota2.pack(pady=8)


botao = ctk.CTkButton(
    janela,
    width=200,
    height=45,
    text='CALCULAR RESULTADO',
    command=calcular,
    fg_color="#2761ff",
    hover_color="#113dff",
    text_color='#fafbfc',
    cursor='hand2',
    font=('Arial', 22)
)
botao.pack(pady=25)

resultado = ctk.CTkLabel(
    janela,
    text='',
    text_color='black',
    font=('arial', 25),

)
resultado.pack(pady=10)

janela.mainloop();

