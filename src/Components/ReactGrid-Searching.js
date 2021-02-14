import React, { useState } from 'react';
import Paper from '@material-ui/core/Paper';
import {
  SearchState,
  IntegratedFiltering,
} from '@devexpress/dx-react-grid';
import {
  Grid,
  Table,
  Toolbar,
  SearchPanel,
  TableHeaderRow,
} from '@devexpress/dx-react-grid-material-ui';

import { generateRows } from './generator';

export default function SearchGrid() {
  const [columns] = useState([
    { name: 'name', title: 'Brand' },
    { name: 'gender', title: 'Size' },
    { name: 'city', title: 'Location Manufactured' },
    { name: 'car', title: 'Materials' },
  ]);

  const [rows] = useState(generateRows({ length: 6 }));

  return (
    <Paper>
      <Grid
        rows={rows}
        columns={columns}
      >
        <SearchState defaultValue="" />
        <IntegratedFiltering />
        <Table />
        <TableHeaderRow />
        <Toolbar />
        <SearchPanel />
      </Grid>
    </Paper>
  );
};
