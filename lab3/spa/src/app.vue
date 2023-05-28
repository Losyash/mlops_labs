<template>
  <div class="container">
    <div class="row py-5">
      <div class="col">
        <h2 class="page-caption">Раскрашивание изображений с использованием нейронных сетей</h2>
      </div>
    </div>

    <div class="card p-4 mb-3">
      <div class="row pb-4">
        <div class="col-12 d-flex justify-content-start pb-3">
          <h5 class="section-caption">Выберите файл</h5>
        </div>

        <div class="col-12 d-flex justify-content-start">
          <u-file :multiple="multiple"
            :mimes="mimes"
            @change="selectFile"
          />
        </div>
      </div>

      <div v-if="inputImage"
        class="row d--flex justify-content-end pb-4"
      >
        <div  class="col-auto">
          <button class="u-button u-green"
            @click="clear"
          >Очистить форму
          </button>
        </div>

        <div  class="col-auto">
          <button class="u-button u-blue"
            @click="upload"
          >Раскрасить изображение
          </button>
        </div>
      </div>
    </div>

    <div v-if="inputImage || outputImage"
      class="card p-4 mb-3"
    >
      <div class="row">
        <div class="col-6">
          <img :src="inputImage"
            class="response-image"
          />
        </div>

        <div class="col-6">
          <img :src="outputImage"
            class="response-image"
          />
        </div>
      </div>
    </div>

    <div v-if="inputImage && outputImage"
      class="card p-4"
    >
      <div class="row d-flex justify-content-center">
        <div class="col-12">
          <USlider :afterImage="outputImage"
            :beforeImage="inputImage"
            :step="0.01"
            :value="50"
          />
        </div>
      </div>
    </div>

    <loading :active="isLoading" 
      :can-cancel="false" 
      :is-full-page="true"
    />
  </div>
</template>

<script setup>
  import { ref, computed } from 'vue';
  import Loading from 'vue3-loading-overlay';
  import axios from 'axios';
  import utils from '@/libs/utils';
  import UFile from '@/components/controls/UFile';
  import URadio from '@/components/controls/URadio';
  import USlider from '@/components/USlider'
  import 'vue3-loading-overlay/dist/vue3-loading-overlay.css';

  const mimes = ['image/png', 'image/jpeg'];
  const multiple = false;

  const files = ref(null);
  const link = ref(null);
  const isLoading = ref(false);

  const outputImage = ref(null);
  const inputImage = ref(null);

  const selectFile = async (data) => {
    outputImage.value = null;
    inputImage.value = null;

    files.value = data;

    const uintdata = await utils.readFileAsArrayBuffer(files.value[0]);
    const filedata = btoa(utils.arrayToString(uintdata))

    inputImage.value = `data:image/jpeg;base64,${filedata}`
  };

  const clear = () => {
    inputImage.value = null;
    outputImage.value = null;
  };

  const upload = async () => {
    isLoading.value = true;

    try {
      const uintdata = await utils.readFileAsArrayBuffer(files.value[0]);
      const filedata = btoa(utils.arrayToString(uintdata))

      const { data } = await axios.post('/file', { file: filedata });
      outputImage.value = `data:image/jpeg;base64,${data}`
    } catch (error) {
      console.log(error)
    };

    isLoading.value = false;
  };
</script>

<style>
  @import 'bootstrap/dist/css/bootstrap.css';
  @import "@/assets/style/style.css";
</style>