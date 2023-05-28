export default {
  readFileAsArrayBuffer(file) {
    return new Promise((resolve, reject) => {
      const fileReader = new FileReader();

      fileReader.onload = (e) => {
        const bytes = new Uint8Array(e.target.result);
        resolve(bytes);
      };

      fileReader.onerror = function(error) {
        reject(error);
      };

      fileReader.readAsArrayBuffer(file);
    });
  },


  readFileAsDataURL(file) {
    return new Promise((resolve, reject) => {
      const fileReader = new FileReader();

      fileReader.onload = (e) => {
        resolve(e.target.result);
      };

      fileReader.onerror = function(error) {
        reject(error);
      };

      fileReader.readAsDataURL(file);
    });
  },


    arrayToString(array) {
      let binary = '';
      const byteLength = array.byteLength;
  
      for (let i = 0; i < byteLength; i++) {
        binary = binary.concat(String.fromCharCode(array[i]));
      };
  
      return binary;
    },


    stringToArray(binary) {
      const binaryLength = binary.length;
      const bytes = new Uint8Array(binaryLength);
  
      for (let i = 0; i < binaryLength; i += 1) {
        let ascii = binary.charCodeAt(i);
        bytes[i] = ascii;
      };
  
      return bytes;
    },


    stringToBase64(binary) {
      return btoa(binary);
    },
  

    base64ToString(base64) {
      return atob(base64);
    },


    toBlob(buffer, mimeType) {
      let data = new Uint8Array(buffer);
      let blob = new Blob([data], {
        type: mimeType
      });
  
      return blob;
    }
};