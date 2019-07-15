import React, { Component } from 'react';
import NoMatch from './components/NoMatch.js';
import Nest from './components/pages/Nest.js';
import Studio from './components/pages/Studio.js';
import Kit from './components/pages/Kit.js';
import Share from './components/pages/Share.js';
import Insights from './components/pages/Insights.js';
import { Route, Redirect, Switch } from 'react-router-dom';

class Router extends Component {

    render() {
        return (
            <div style={{ height: '100%', position: 'relative' }}>
                <Switch>

                    <Route path="/students/nest/:tab" render={({ match, history }) => <Nest {...this.props} match={match} history={history} />} />
                    <Redirect from="/students/nest" exact to="/students/nest/home"/>
                    <Redirect from="/students" exact to="/students/nest/home"/>
                    
                    <Route path="/students/studio" exact render={({ match, history }) => <Studio {...this.props} match={match} history={history}/>}/>
                    <Route path="/students/kit" exact render={({ match, history }) => <Kit {...this.props} match={match} history={history}/>}/>
                    <Route path="/students/share" exact render={({ match, history }) => <Share {...this.props} match={match} history={history}/>}/>
                    <Route path="/students/insights" exact render={({ match, history }) => <Insights {...this.props} match={match} history={history}/>}/>

                
                    <Route component={NoMatch} />
                </Switch>

            </div>
        )
    }
}

export default Router;