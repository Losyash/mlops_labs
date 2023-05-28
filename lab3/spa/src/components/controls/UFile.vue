<template>
  <label class="upload-area"
    @drop.stop.prevent="drop"
    @dropover.stop.prevent="dropover"
  >
    <span class="upload-text">Перетащите сюда файл или нажмите для выбора файла(ов)</span>

    <input :accept="accept"
      :multiple="multiple"
      class="upload-input"
      type="file"
      @input="change"
    />
</label>
</template>

<script setup>
  import { ref, computed } from 'vue';

  const props = defineProps({
    mimes: {
      type: Array,
      required: true
    },
    disabled: {
      type: Boolean,
      default: true
    },
    multiple: {
      type: Boolean,
      default: false
    }
  });

  const emits = defineEmits([ 'change' ]);
  const mimes = ref(props.mimes);

  const change = (e) => {
    emits('change', [...e.target.files]);
  };

  const accept = computed(() => {
    if (mimes && mimes.length) {
      return mimes.join(',');
    } else {
      return null;
    };
  });

  const drop = (e) => emits('change', e.dataTransfer.files);
</script>

<style scoped>
  .upload-area {
    align-items: center;
    border-radius: 5px;
    border: 1px dashed #1E4391;
    display: flex;
    flex-wrap: wrap;
    height: 80px;
    justify-content: center;
    max-width: 100%;
    padding: 20px 10px;
    position: relative;
    transition: 0.2s;
    width: 100%;
  }

  .upload-area:hover {
    border: 1px dashed green;
  }

  .upload-area:hover .upload-text {
    color: green
  }

  .upload-input {
    bottom: 0;
    cursor: pointer;
    height: 100%;
    left: 0;
    opacity: 0;
    position: absolute;
    right: 0;
    top: 0;
    width: 100%;
  }

  .upload-icon {
    color: #40a9ff;
    font-size: 30px;
  }

  .upload-text {
    display: flex;
    font-family: "Roboto Regular", sans-serif;
    justify-content: center;
    width: 100%;
  }
</style>