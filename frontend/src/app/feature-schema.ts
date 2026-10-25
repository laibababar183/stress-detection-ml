export type Feature = {
  name: string;
  label: string;
  kind: 'number' | 'category';
  required: boolean;
  options?: string[];
  min?: number;
  max?: number;
};

export const FEATURES: Feature[] = [
  { name: 'MEAN_RR', label: 'Mean RR (ms)', kind: 'number', required: true, min: 0 },
  { name: 'SDRR', label: 'SDRR (ms)', kind: 'number', required: true, min: 0 },
  { name: 'RMSSD', label: 'RMSSD (ms)', kind: 'number', required: true, min: 0 },
];