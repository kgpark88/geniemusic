<template>
  <div id="appRoot">
    <template>
      <v-app id="inspire" class="app" >   
        <Toolbar></Toolbar>
        <v-main>
          <v-fade-transition mode="out-in">
            <router-view></router-view>
          </v-fade-transition>
          <Footer></Footer>
        </v-main>
      </v-app>
    </template>  
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
    Toolbar: () => import('@/components/MainToolbar'),
    Footer: () => import('@/components/MainFooter'),
  },
  data () {
    return {
      fullscreen: false,
    }
  },
  methods: {
    home: function() {
      const path = `/`
      if (this.$route.path !== path) this.$router.push(path)
    }
  }
};
</script>
