<template>
    <div class="w-max m-auto">
        <button @click="open = true">
            <div class="grid w-max">
                    <div class="text-center"><p>{{getPosition(player)}}</p></div>
                    <div class="w-16 h-16 sm:w-20 sm:h-20 bg-cover m-auto" :class="team_path" :id="player.position"></div>
                    <div class="text-cente grid grid-rows-2 w-[75px] sm:w-[100px] text-xs sm:text-base">
                        <div v-if="player.status == 'i'" class="text-center bg-red-500 text-white px-1"><p>{{player.web_name}}</p></div>
                        <div v-else-if="player.status == 'd'" class="text-center bg-orange-500 text-white px-1"><p>{{player.web_name}}</p></div>
                        <div v-else class="text-center bg-black text-white px-1"><p>{{player.web_name}}</p></div>
                        <div class="text-center bg-white"><p>{{ player.total_points }}</p></div>
                </div>
            </div>
        </button>
    </div>

    <TransitionRoot as="template" :show="open">
      <Dialog class="relative z-10" @close="open = false">
        <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>
  
        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200" leave-from="opacity-100 translate-y-0 sm:scale-100" leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel class="relative transform overflow-hidden rounded-lg bg-white shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
                <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                  <div class="sm:items-start">
                    <!-- <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                      
                    </div> -->
                    <div class="mt-3 text-center sm:ml-4 sm:mt-0">
                    <button type="button" class="mt-3 absolute top-1 right-1 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto" @click="open = false" ref="cancelButtonRef">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" class="Dialog__CloseIcon-sc-5bogmv-3 ehxuGi"><polygon fill-rule="evenodd" points="16 13.56 10.441 8 16 2.44 13.56 0 8.001 5.56 2.441 0 .001 2.44 5.561 8 0 13.56 2.44 16 8.001 10.44 13.56 16"></polygon></svg>

                    </button>
                      <DialogTitle as="h3" class="text-2xl font-semibold leading-6 text-gray-900 pb-2">
                        {{ player.first_name }} {{ player.second_name }}
                      </DialogTitle>
                      <div v-for="game in player.explain_points" class="pt-5 border-t-2">
                        <div class="grid grid-cols-3 text-center justify-center w-1/2 m-auto">
                          <div class="m-auto">{{ game.team_h }}</div>
                          <div class="grid grid-cols-2 bg-black text-white p-1 text-2xl">
                            <div>{{ game.team_h_score }}</div>
                            <div>{{ game.team_a_score }}</div>
                          </div>
                          <div class="m-auto">{{ game.team_a }}</div>
                        </div>
                        <table class="m-auto mt-3">
                          <thead>
                            <tr>
                              <th>Statistics</th>
                              <th>Value</th>
                              <th>Points</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr v-for="info in game.stats">
                              <td>
                                {{ info.identifier }}
                              </td>
                              <td>
                                {{ info.value }}
                              </td>
                              <td>
                                {{ info.points }}
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
<!--                 <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                   <button type="button" class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 sm:ml-3 sm:w-auto" @click="open = false">Deactivate</button>
                  <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto" @click="open = false" ref="cancelButtonRef">Cancel</button>
                </div> -->
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

</template>

<script setup>
const props = defineProps({
  player: {
    type: Object,
    required: true,
  },
});
const {player} = props;
const team_path = "bg-[url('/assets/img/" + player.team + ".png')]"
function getPosition(player){
    if (player.element_type == 1){
        return "GKP"
    } else if(player.element_type == 2){
        return "DEF"
    } else if(player.element_type == 3){
        return "MID"
    }
    else{
        return "ATT"
    }
}
import { ref } from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
const open = ref(false)
</script>