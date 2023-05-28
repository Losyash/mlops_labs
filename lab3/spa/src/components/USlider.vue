<template>
  <div ref="imageWrapper"
    class="images-wrapper"
  >
    <img :src="beforeImage"
      class="before-image"
    >
      <div :style="{ width: `${compareWidth}%`}"
        class="compare-overlay"
      >
        <img :src="afterImage"
          :style="{ width: `${width}px` }"
          class="after-image"  
        >
      </div>

      <input :step="step"
        :value="compareWidth"
        class="compare__range"
        max="100"
        min="0"
        tabindex="-1"
        type="range"
        @input="onInput"
      />

      <div :style="{ left: `${compareWidth}%` }"
        class="handle-wrap"
      >
        <div class="handle">
          <svg class="handle__arrow handle__arrow--l"
            fill="none"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            stroke="currentColor"
            viewBox="0 0 24 24"
            width="24" height="24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <polyline points="15 18 9 12 15 6"/>
          </svg>

          <svg class="handle__arrow handle__arrow--r"
            fill="none"
            height="24"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            stroke="currentColor"
            viewBox="0 0 24 24"
            width="24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <polyline points="9 18 15 12 9 6"/>
          </svg>
        </div>
      <span class="handle-line" />
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      value: {
        type: Number,
        default: 50
      },
      beforeImage: {
        type: String,
        default: ''
      },
      afterImage: {
        type: String,
        default: ''
      },
      step: {
        type: Number,
        default: 0.1
      }
    },
    data() {
      return {
        width: null,
        compareWidth: this.value,
      }
    },
    mounted() {
      this.width = this.$refs.imageWrapper.getBoundingClientRect().width
      window.addEventListener('resize', this.onResize)
    },
    destroyed() {
      window.removeEventListener('resize', this.onResize)
    },
    methods: {
      onInput(e) {
        this.compareWidth = e.target.value
      },
      onResize() {
        this.width = this.$refs.imageWrapper.getBoundingClientRect().width
      }
    }
  };
</script>
  
<style scoped>
  .images-wrapper {
    position: relative;
    width: 100%;
  }

  .compare-overlay {
    height: auto;
    overflow:hidden;
    position: absolute;
    top:0;
  }

  .before-image,
  .after-image {
    height: auto;
    width: 100%;
  }

  .after-image {
    position: relative;
    width: 50%;
    z-index: 2;
  }

  .compare__range {
    background: rgba(0,0,0,.4);
    cursor: ew-resize;
    height: 50px;
    left: 0;
    opacity: 0;
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    z-index: 999;
  }

  .handle__arrow {
    position: absolute;
    width: 20px;
  }

  .handle__arrow--l {
    left:0;
  }

  .handle__arrow--r {
    right:0;
  }

  .handle-wrap {
    align-items: center;
    display: flex;
    height: 100%;
    justify-content: center;
    position: absolute;
    top: 50%;
    transform: translate(-50%, -50%);
    z-index: 5;
  }

  .handle {
    align-items: center;
    background: #1E4391;
    border-radius: 50%;
    color: white;
    display: flex;
    height: 30px;
    justify-content: center;
    width: 30px;
  }

  .handle-line {
    background: #1E4391;;
    content: '';
    height: 100%;
    pointer-events:none;
    position: absolute;
    top:0;
    user-select:none;
    width: 2px;
    z-index: 4;
  }

  @media screen and (max-width: 568px) {
    .handle {
      height: 25px;
      width: 25px;
    }

    .handle__arrow {
      width: 20px;
    }
  }

  @media screen and (max-width: 480px) {
    .handle {
      height: 15px;
      width: 15px;
    }

    .handle__arrow {
      width: 10px;
    }
  }
</style>