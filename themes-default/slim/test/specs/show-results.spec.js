import Vuex, { Store } from 'vuex';
import VueRouter from 'vue-router';
import vueCookies from 'vue-cookies';
import { createLocalVue, shallowMount } from '@vue/test-utils';
import { ShowResults } from '../../src/components';
import configModule from '../../src/store/modules//config';
import historyModule from '../../src/store/modules/history';
import providerModule from '../../src/store/modules/provider';
import show from '../__fixtures__/show-detailed';
import episodeHistory from '../__fixtures__/episode-history';
import fixtures from '../__fixtures__/common';
import provider from '../__fixtures__/providers';

describe('ShowResults.test.js', () => {
    let localVue;
    let store;
    let { state } = fixtures;
    state = {
        ...state,
        ...{ provider },
        ...{ history: {
            history: [],
            page: 0,
            showHistory: {},
            episodeHistory: {
                tvdb5692427: {
                    s04e06: episodeHistory
                }
            }
        } },
        ...{ search: {
            queueitems: []
        } }
    };

    beforeEach(() => {
        localVue = createLocalVue();
        localVue.use(Vuex);
        localVue.use(VueRouter);
        localVue.use(vueCookies);

        store = new Store({
            modules: {
                config: configModule,
                history: historyModule,
                provider: providerModule
            }
        });
        store.replaceState(state);
    });

    it('renders show-results component with results', async () => {
        const wrapper = shallowMount(ShowResults, {
            localVue,
            store,
            propsData: {
                show,
                season: 4,
                episode: 6
            }
        });

        await wrapper.vm.$nextTick();
        expect(wrapper.element).toMatchSnapshot();
    });
});