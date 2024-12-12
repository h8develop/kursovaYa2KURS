import React from 'react';

function Dashboard() {
return (
<div>
    <h2>Analytics Dashboard</h2>
    <iframe src="http://grafana.local/d-solo/ce6gdaqyi2eiof/total-ads?orgId=1&refresh=10s&from=1733798169477&to=1733798469478&timezone=browser&panelId=1&__feature.dashboardSceneSolo" width="450" height="200" frameborder="0"></iframe>
</div>
);
}

export default Dashboard;