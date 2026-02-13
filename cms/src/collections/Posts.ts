import type { CollectionConfig } from 'payload'

export const Posts: CollectionConfig = {
  slug: 'posts',
  admin: {
    useAsTitle: 'title',
    defaultColumns: ['title', 'category', 'status', 'publishedAt'],
    group: 'Blog',
  },
  access: {
    read: () => true,
  },
  fields: [
    {
      name: 'title',
      type: 'text',
      required: true,
      label: '標題',
    },
    {
      name: 'slug',
      type: 'text',
      required: true,
      unique: true,
      label: 'Slug',
      admin: {
        description: 'URL path (e.g. tsmc-intrinsic-value-2026)',
      },
    },
    {
      name: 'content',
      type: 'richText',
      required: true,
      label: '內容',
    },
    {
      name: 'excerpt',
      type: 'textarea',
      label: '摘要',
      admin: {
        description: 'SEO description and preview text (max 160 chars)',
      },
    },
    {
      name: 'category',
      type: 'relationship',
      relationTo: 'categories',
      label: '分類',
    },
    {
      name: 'coverImage',
      type: 'upload',
      relationTo: 'media',
      label: '封面圖片',
    },
    {
      name: 'status',
      type: 'select',
      required: true,
      defaultValue: 'draft',
      label: '狀態',
      options: [
        { label: 'Draft', value: 'draft' },
        { label: 'Published', value: 'published' },
      ],
    },
    {
      name: 'publishedAt',
      type: 'date',
      label: '發布日期',
      admin: {
        date: { pickerAppearance: 'dayAndTime' },
        condition: (data) => data?.status === 'published',
      },
    },
  ],
}
