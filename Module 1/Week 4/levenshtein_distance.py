import streamlit as st


def levenshtein(source, target):
    # Get size of the strings
    m = len(source)
    n = len(target)

    # Create a matrix to store the distance
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # Fill in the first row with insertions distance
    for i in range(m+1):
        dp[i][0] = i

    # Fill in the first column with deletions distance
    for j in range(n+1):
        dp[0][j] = j

    # Fill in the rest of the matrix, starting from the second row and column
    for i in range(1, m+1):
        for j in range(1, n+1):
            # If the last characters are the same, the cost is 0
            if source[i - 1] == target[j - 1]:
                sub_cost = 0
            else:
                sub_cost = 1

            dp[i][j] = min(dp[i-1][j] + 1,  # Deletion
                           dp[i][j-1] + 1,  # Insertion
                           dp[i-1][j-1] + sub_cost)  # Substitution

    return dp[m][n]


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


vocabs = load_vocab(file_path='Module 1\Week 4\data\\vocab.txt')


def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')

    if st.button("Compute"):

        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein(word, vocab)

        # sorted by distance
        sorted_distences = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distences.keys())[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)

        col2.write('Distances:')
        col2.write(sorted_distences)


if __name__ == "__main__":
    main()
