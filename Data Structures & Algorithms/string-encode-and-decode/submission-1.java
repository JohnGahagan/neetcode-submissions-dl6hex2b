class Solution {

    public String encode(List<String> strs) {
        //each string in the list
        //encode each one
        //when ',' is seen take the element after it and before it too
        //remove these 3 elements per ","
        
        StringBuilder encoded = new StringBuilder();
        for (String str : strs) {
            encoded.append(str.length()).append(",").append(str);
        }
        return encoded.toString();
    }

    public List<String> decode(String str) {
        //use the encoded List
        //decode it
        List<String> decoded = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int delimiterIndex = str.indexOf(",", i);
            
            int length = Integer.parseInt(str.substring(i, delimiterIndex));
            String str2 = str.substring(delimiterIndex + 1, delimiterIndex + 1 + length);
            decoded.add(str2);

            i = delimiterIndex + 1 + length;
                    }
                    return decoded;
    }
}
