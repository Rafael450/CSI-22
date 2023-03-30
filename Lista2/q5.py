def matrix_mult(matrix1, matrix2):

    if len(matrix1[0]) != len(matrix2): 
        return None
    
    final = []
    for row in matrix1:
        mid = []

        for j in range(len(matrix2[0])):
            m_sum = 0

            for i in range(len(row)):
                m_sum += row[i]*matrix2[i][j]

            mid.append(m_sum)
            
        final.append(mid)

    return final