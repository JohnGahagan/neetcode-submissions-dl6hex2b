class Solution {
    public boolean isAnagram(String s, String t) {
        // Check if lengths are different; if so, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Convert strings to char arrays
        char[] arrS = s.toCharArray();
        char[] arrT = t.toCharArray();
        
        // Sort the char arrays
        bubbleSort(arrS);
        bubbleSort(arrT);
        
        // Compare sorted char arrays
        for (int i = 0; i < arrS.length; i++) {
            if (arrS[i] != arrT[i]) {
                return false;
            }
        }
        return true;
    }

    // Bubble sort implementation
    private void bubbleSort(char[] arr) {
        boolean swapped;
        for (int i = 0; i < arr.length - 1; i++) {
            swapped = false;
            for (int j = 0; j < arr.length - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    char temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) break;
        }
    }
}
