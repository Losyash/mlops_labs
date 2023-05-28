<template>
  <label class="u-form-radio">
    <input v-model="localValue"
      :value="value"
      :name="name"
      type="radio" 
    />

    <span class="u-form-radio-checkmark"></span>
    <span class="u-form-radio-label">{{ title }}</span>
  </label>
</template>

<script setup>
  import { computed } from 'vue';

  const props = defineProps({
    modelValue: {
      type: [String, Number]
    },
    value: {
      required: true
    },
    title: {
      type: String
    },
    name: {
      type: String
    }
  });

  const emits = defineEmits([
    'update:modelValue'
  ]);

  const localValue = computed({
    get() {
      return props.modelValue;
    },
    set(value) {
      emits('update:modelValue', value)
    }
  });
</script>