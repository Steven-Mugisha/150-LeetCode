class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        
       
        rows, cols = len(img), len(img[0])
        res = [[0]*cols for _ in range(rows)]

        for row in range (rows):
            for col in range(cols):
                # print(img[row][col])
                total_sum, count = 0, 0

                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        if r < 0 or r >= rows or c < 0 or c >= cols:
                            continue
                        else:
                            total_sum += img[r][c]
                            count += 1
                if count > 0:
                    avg = total_sum//count
                    res[row][col] = avg

        return res

        