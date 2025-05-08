/*
O código a seguir não trata problemas como não conseguir realizar o realloc (retornando NULL) ou então um gerenciamento melhor em relação a capacidade disponível com a quantidade de alunos 
*/
#include <stdio.h>
#include <stdlib.h>

struct Aluno
{
    int matricula;
    char sexo;
    int idade;
};

typedef struct Aluno t_Aluno;

void cadastrar_aluno(t_Aluno **alunos, int *n_alunos) 
{
    *alunos = (t_Aluno*) realloc(*alunos, (*n_alunos + 1) * sizeof(t_Aluno));

    printf("Adicionando um novo aluno...\n");
    printf("Matricula: ");
    scanf("%d", &(*alunos)[*n_alunos].matricula);
    printf("Sexo (M/F): ");
    scanf(" %c", &(*alunos)[*n_alunos].sexo);
    printf("Idade: ");
    scanf("%d", &(*alunos)[*n_alunos].idade);

    (*n_alunos)++;
    printf("Novo aluno cadastrado com sucesso.\n");
}

void alterar_aluno(t_Aluno *alunos, int n_alunos)
{
    int matricula;
    printf("Digite a matricula do aluno que deseja alterar: ");
    scanf("%d", &matricula);

    for (int i = 0; i < n_alunos; i++)
    {
        if (matricula == (alunos)[i].matricula)
        {
            printf("Aluno encontrado!");
            printf("Matricula: %d\n", (alunos)[i].matricula);
            printf("Sexo (antes %c): ", (alunos)[i].sexo);
            scanf(" %c", &(alunos)[i].sexo);
            printf("Idade (antes %d): ", (alunos)[i].idade);
            scanf("%d", &(alunos)[i].idade);

            printf("Cadastro alterado com sucesso.\n");
            return;
        }
    }
    printf("Aluno com matricula (%d) não foi encontrado.\n", matricula);
}

void excluir_aluno(t_Aluno **alunos, int *n_alunos)
{
    int matricula;
    printf("Digite a matricula do aluno que deseja excluir: ");
    scanf("%d", &matricula);

    for (int i = 0; i < *n_alunos; i++)
    {
        if (matricula == (*alunos)[i].matricula)
        {
            printf("Aluno encontrado!\n");

            for (int j = i; j < *n_alunos - 1; j++)
            {
                (*alunos)[j] = (*alunos)[j + 1];
            }
            
            *n_alunos -= 1;
            *alunos = (t_Aluno*) realloc(*alunos, *n_alunos * sizeof(t_Aluno));

            printf("Aluno excluido com sucesso.\n");
            return;
        }
    }
    printf("Aluno com matricula (%d) não foi encontrado.\n", matricula);
}

void listar_alunos(t_Aluno *alunos, int n_alunos)
{
    printf("Lista de alunos (Total: %d):\n", n_alunos);

    for (int i = 0; i < n_alunos; i++)
    {
        printf("\tAluno %d\n", i + 1);
        printf("\t\tMatricula: %d\n", alunos[i].matricula);
        printf("\t\tSexo: %c\n", alunos[i].sexo);
        printf("\t\tIdade: %d\n", alunos[i].idade);
    }
}

int main(int argc, char **argv) 
{
    int n_alunos = 0;
    t_Aluno *alunos;
    int escolha;

    cadastrar_aluno(&alunos, &n_alunos);
    for (;;) {
        escolha = 0;
        printf("BANCO DE DADOS DE ALUNOS\n\n");
        printf("1 - Cadastrar um aluno\n");
        printf("2 - Alterar um aluno\n");
        printf("3 - Excluir um aluno\n");
        printf("4 - Listar todos os alunos\n");
        printf("5 - Sair\n");
        printf("Escolha: ");
        scanf("%d", &escolha);
        switch (escolha)
        {
            case 1:
                cadastrar_aluno(&alunos, &n_alunos);
                break;
            case 2:
                alterar_aluno(alunos, n_alunos);
                break;
            case 3:
                excluir_aluno(&alunos, &n_alunos);
                break;
            case 4:
                listar_alunos(alunos, n_alunos);
                break;
            default:
                printf("Programa encerrado.");
                free(alunos);
                return 0;
        }
    }
}