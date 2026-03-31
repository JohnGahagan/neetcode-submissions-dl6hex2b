class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Create arrays to track digits in rows, columns, and boxes
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];
        
        // Traverse the board
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char current = board[i][j];
                
                // If the cell is not empty
                if (current != '.') {
                    int num = current - '1'; // Convert char '1'-'9' to index 0-8
                    int boxIndex = (i / 3) * 3 + (j / 3); // Calculate box index
                    
                    // Check if the number is already seen in the row, column, or box
                    if (rows[i][num] || cols[j][num] || boxes[boxIndex][num]) {
                        return false; // Duplicate found
                    }
                    
                    // Mark the number as seen in the row, column, and box
                    rows[i][num] = true;
                    cols[j][num] = true;
                    boxes[boxIndex][num] = true;
                }
            }
        }
        
        return true; // All rows, columns, and boxes are valid
    }
}
